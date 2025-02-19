from flask import Flask, render_template, request, jsonify, Blueprint, redirect, url_for
import requests

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

# 메인 페이지 렌더링
@kakao_bp.route('/showstore')
def showstore():

    foodname = request.args.get('foodname')
    if foodname:
        return render_template('kakao/kakao-board4.html', foodname=foodname)
    else:
        return redirect(url_for("main.index"))

# # 키워드 검색 API
# @kakao_bp.route('/search', methods=['GET'])
# def search():
#     query = request.args.get('query')
#     if query:
#         return f"검색어: {query}에 대한 결과를 보여줍니다."
#     else:
#         return "검색어를 입력해주세요."

# app_bp =Blueprint("kakao",__name__, url_prefix="/kakao/showstore")

# @app.route("/store/<foodname>")
# def show_store(foodname):
#     if not foodname:
#         return "음식 이름이 필요합니다!", 400
#     return render_template("kako-board4.html", foodname=foodname)

@kakao_bp.route("/search-store/", methods=["GET"])
def search_store():
    query = request.args.get("query")
    x = request.args.get("x")
    y = request.args.get("y")
    radius = request.args.get("radius", 2000)

    print("=====================================>", query)

    headers = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}
    params = {"query": query, "x": x, "y": y, "radius": radius, "sort": "distance", "size": 15 }
    url = "https://dapi.kakao.com/v2/local/search/keyword.json"

    response = requests.get(url, headers=headers, params=params)

    final_result = {}
    if response.status_code == 200:
        data = response.json()
        places = data["documents"] 
        # for idx, place in enumerate(places, start=1):
        #     print(f"{idx}. {place['place_name']} - {place['address_name']} (거리: {place['distance']}m)")
        result = [ {'place_name':place['place_name'], 'lat': place['y'], 'lng': place['x']} for place in places ]
        final_result = { "result": "success", "data": result }
    else:
        print(f"Error {response.status_code}: {response.text}")
        final_result = { "result": "fail", "data": [] }
    
    return jsonify(final_result)





