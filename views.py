import os
from flask import Flask,request
from flask.json import jsonify
from infer import Inference
from PIL import Image
import datetime

app = Flask(__name__)
model = Inference()

@app.route("/determine-rotation", methods=[ "POST"])
def predict():
    file = request.files["file"]

    filename = str(datetime.datetime.now())+".jpg"

    input_path = os.path.join("/tmp/", filename)

    file.save(input_path)
    
    img = Image.open(input_path)

    img = img.resize((400, 400))

    img.save(input_path)

    model_name = request.form["model"].lower()

    angle = model.predict(model_name, input_path)
    return jsonify(angle=int(angle))
