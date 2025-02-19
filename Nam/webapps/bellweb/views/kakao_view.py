from flask import Flask, render_template, request, jsonify, Blueprint
import requests

app = Flask(__name__)

# Blueprint 생성
kakao_bp = Blueprint("kakao", __name__, url_prefix="/kakao")

KAKAO_API_KEY = "74a779368cf2713c3d5a3cc365f45edf"

def search_restaurants(lat, lng):
    """카카오 장소 검색 API를 사용해 주변 맛집 검색"""
    url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    headers = {"Authorization": f"KakaoAK {'74a779368cf2713c3d5a3cc365f45edf'}"}
    params = {
        "query": "맛집",
        "x": lng,
        "y": lat,
        "radius": 1000,
        "size": 5
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

# 메인 페이지 렌더링
@kakao_bp.route('/')
def home():
    return render_template('kakao/kakao-board4.html')

# 키워드 검색 API
@kakao_bp.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if query:
        return f"검색어: {query}에 대한 결과를 보여줍니다."
    else:
        return "검색어를 입력해주세요."

@app.route("/kakao-api", methods=["GET"])
def kakao_api():
    query = request.args.get("query")
    x = request.args.get("x")
    y = request.args.get("y")
    radius = request.args.get("radius", 2000)

    headers = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}
    params = {"query": query, "x": x, "y": y, "radius": radius, "category_group_code": "FD6"}
    url = "https://dapi.kakao.com/v2/local/search/keyword.json"

    response = requests.get(url, headers=headers, params=params)
    return jsonify(response.json().get("documents", []))





