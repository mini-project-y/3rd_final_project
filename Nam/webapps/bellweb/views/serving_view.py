from flask import Blueprint, render_template
from flask import request, jsonify
from ..db_utils import serving_util

serving_bp = Blueprint("serving", __name__, url_prefix="/serving")

@serving_bp.route("/index/")
def index():
    return render_template("serving/index.html")

@serving_bp.route("/predict/", methods=['POST'])
def predict():
    # import datetime
    # return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    from PIL import Image
    from tensorflow import keras as tf_keras
    import numpy as np
    from pathlib import Path
    import oauthlib
    import os
    from tensorflow.keras.applications.resnet import preprocess_input
    import pandas as pd

    # 요청 데이터 읽기 ( 이미지 파일 데이터 읽기 )
    files = request.files # 파일 데이터 읽기 ( cf. request.args, request.form )
    if 'img_input' not in files: # img_input 입력 요소가 없는 경우
        return jsonify({
            "result": "fail",
            "message": "No file part"
        }), 400
    
    file = files['img_input']
    if len(file.filename) == 0:      # img_input에 파일이 선택되지 않은 경우
        return jsonify({
            "result": "fail",
            "message": "File not selected"
        }), 400
    
    image_input = Image.open(file)  # 파일을 이미지 형식으로 변경
    image_input = image_input.resize((256, 256))    # 모델의 입력크기에 맞게 이미지 크기 변경
    image_array = tf_keras.utils.img_to_array(image_input)
    # image_array /= 255  # 모델의 입력 형식에 맞게 데이터 변경 : 0 ~ 255 -> 0 ~ 1
    # image_array = np.expand_dims(image_array, 0) # 단일 입력을 배치 입력으로 변환
    image_array = preprocess_input(image_array)
    image_array = np.expand_dims(image_array, 0)

    rpath = serving_bp.root_path    # Blueprint가 존재하는 경로
    root_path = Path(rpath).parent  # rpath의 부모 경로  
    sub_path = 'serving_models/model.keras'
    food_model = tf_keras.models.load_model(os.path.join(root_path, sub_path))

    predictions = food_model.predict(image_array)
    predicted_class = int(np.argmax(predictions, axis=1))
    confidence = float(np.max(predictions))

    recipes = serving_util.select_recipe(predicted_class)
    if not recipes:
        return jsonify({
            "result": "success",
            "message": "No recipes found for the predicted class.",
            "predicted_class": predicted_class,
            "confidence": confidence,
            "recipes": []
        })

    # 조회 결과를 JSON 형식으로 반환
    recipe_list = [
        {"name": row[0], "ingredients": row[1], "recipe": row[2], "food_name_eng": row[3]} for row in recipes
    ]
    return jsonify({
        "result": "success",
        "message": "",
        "predicted_class": predicted_class,
        "confidence": confidence,
        "recipes": recipe_list
    })