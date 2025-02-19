import requests
from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv

# 환경변수 로드
load_dotenv()
KAKAO_API_KEY = os.getenv("KAKAO_API_KEY")

app = Flask(__name__)

def search_restaurants(lat, lng):
    """카카오 장소 검색 API를 사용해 주변 맛집 검색"""
    url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    headers = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}
    params = {
        "query": "맛집",  # 검색어
        "x": lng,
        "y": lat,
        "radius": 500,  # 반경 500m
        "size": 5  # 최대 5개 결과
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

@app.route('/search-by-coordinates', methods=['GET'])
def search_by_coordinates():
    """사용자가 보낸 좌표를 기반으로 맛집 검색"""
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    if not lat or not lng:
        return jsonify({"error": "좌표를 입력하세요"}), 400

    data = search_restaurants(lat, lng)
    return jsonify(data["documents"])

if __name__ == '__main__':
    app.run(debug=True)
