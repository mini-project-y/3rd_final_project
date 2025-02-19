from flask import Blueprint, render_template, request, jsonify
import openai
from openai import OpenAIError
from ..db_utils import serving_util
from PIL import Image
from tensorflow import keras as tf_keras
import numpy as np
from pathlib import Path
import os
from tensorflow.keras.applications.resnet import preprocess_input

serving_bp = Blueprint("serving", __name__, url_prefix="/serving")

import openai

client = openai.OpenAI()

def translate_text(text):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Translate the following Korean text into English while maintaining its original format:"},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content.strip()
    except openai.OpenAIError as e:
        print(f"Translation Error: {e}")  # 오류 로그 기록
        return "Translation failed"


@serving_bp.route("/index/")
def index():
    return render_template("serving/index.html")

@serving_bp.route("/predict/", methods=['POST'])
def predict():
    files = request.files
    if 'img_input' not in files or files['img_input'].filename == '':
        return jsonify({"result": "fail", "message": "No file selected"}), 400
    
    file = files['img_input']
    image_input = Image.open(file).resize((256, 256))
    image_array = preprocess_input(tf_keras.utils.img_to_array(image_input))
    image_array = np.expand_dims(image_array, 0)

    root_path = Path(serving_bp.root_path).parent  
    food_model = tf_keras.models.load_model(os.path.join(root_path, 'serving_models/model.keras'))
    
    predictions = food_model.predict(image_array)
    predicted_class = int(np.argmax(predictions, axis=1))
    confidence = float(np.max(predictions))
    
    recipes = serving_util.select_recipe(predicted_class)
    if not recipes:
        return jsonify({"result": "success", "predicted_class": predicted_class, "confidence": confidence, "recipes": []})
    
    recipe_list = []
    for row in recipes:
        recipe_kr = row[2]
        ingredients_kr = row[1]
        recipe_en = translate_text(recipe_kr) if recipe_kr else ""
        ingredients_en = translate_text(ingredients_kr) if ingredients_kr else ""
        
        recipe_list.append({
            "id": row[0],
            "name": row[0],
            "food_name_eng": row[3],
            "ingredients_kr": ingredients_kr,
            "ingredients": ingredients_en,
            "recipe_kr": recipe_kr,
            "recipe": recipe_en
        })
    
    return jsonify({
        "result": "success",
        "predicted_class": predicted_class,
        "confidence": confidence,
        "recipes": recipe_list
    })