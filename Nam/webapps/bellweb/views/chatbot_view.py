from flask import Blueprint, request, jsonify, session, current_app
from openai import OpenAI
from ..db_utils import chatbot_util

chatbot_bp = Blueprint("chatbot", __name__, url_prefix="/chatbot")

# os.environ['OPENAI_API_KEY'] = ""
# cmd 창에서 set OPENAI_API_KEY=api_key
client = OpenAI() # 환경변수에 저장된 api_key를 사용


@chatbot_bp.route("/chat-text/", methods=['POST'])
def handle_chat_text():
    json_data = request.get_json()
    message = json_data.get('message')
    
    memberid = session.get("memberid")

    member_info = chatbot_util.select_member_information(memberid)
    print("member_info:", member_info)
    gender, nationality, vegetarian_type = member_info[0]
    
    allergic_foods = chatbot_util.select_member_allergic(memberid)

    
    favorite_taste = chatbot_util.select_favorit_taste(memberid)
    disliked_taste = chatbot_util.select_disliked_taste(memberid)
    excluded_meat = chatbot_util.select_excluded_meat(memberid)

    # helper = current_app.config['CHROMADB_HELPER']
    # selected_recruits = helper.query_similar_documents(message, top_k=5)
    
    # recruit_list_str = [f'{idx+1}. {recruit}\n' for idx, recruit 
    #                     in enumerate(selected_recruits['documents'][0])]

    prompt = f"""             
             아래의 고려사항과 지시사항을 적극적으로 반영해서 질문에 대한 답변을 만들어 주세요.

             ###지시사항###
             1. 사용자의 취향에 맞춰서 음식과 식단을 추천하는 챗봇입니다.
             2. 고려사항을 적극 반영해서 음식을 추천해주세요
             
             ###고려사항###
             1. 사용자는 {gender}이다
             2. 사용자는 {nationality}이란 나라에서 태어난 사람이다.
             3. 사용자의 유형은 {vegetarian_type}이다.
             4. 사용자는 {allergic_foods}에 대한 알러지가 있다.
             5. 사용자는 {favorite_taste} 맛을 좋아한다.
             6. 사용자는 {disliked_taste} 맛을 싫어한다.
             7. 사용자는 고기 종류 중에서 {excluded_meat}는 먹지 못한다.

             질문 : {message}
             답변 : """

    chat_history = session.get('chat-history', [])
    if len(chat_history) == 0: # if chat_history:
        chat_history.append({ "role": "system", "content": "당신은 모든 정보를 잘 알고 있는 친절한 안내자입니다. 질문에 대해 가능한 간결하게 답변해야 합니다." })

    chat_history.append({ "role": "user", "content": prompt })

    completion = client.chat.completions.create(
        model="chatgpt-4o-latest",
        messages=chat_history,
        n=1,
        temperature=1.5
    )

    last_chat = chat_history[-1]
    last_chat['content'] = message
    
    chat_history.append({ "role": "assistant", "content": completion.choices[0].message.content })

    session['chat-history'] = chat_history

    return jsonify({ 'message' : completion.choices[0].message.content })


@chatbot_bp.route("/reload-chat-history/")
def reload_chat_history():
    chat_history = session.get("chat-history", [])

    if len(chat_history) == 0: # if chat_history:
        chat_history.append({ "role": "system", "content": "당신은 모든 정보를 잘 알고 있는 친절한 안내자입니다. 질문에 대해 가능한 간결하게 답변해야 합니다." })

    session['chat-history'] = chat_history

    return jsonify( chat_history[1:] if len(chat_history) > 1 else [] )


@chatbot_bp.route("/audio-to-text/", methods=['POST'])
def audio_to_text():
    audio = request.files.get("audio")
    audio.save(audio.filename)

    with open(audio.filename, 'rb') as f:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=f
        )
    print(transcription.text)
    return transcription.text