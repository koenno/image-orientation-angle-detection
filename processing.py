from PIL import Image
import numpy as np
from transformers import ViTFeatureExtractor
feature_extractor = ViTFeatureExtractor.from_pretrained('google/vit-base-patch16-224')

def preprocess(model_name, image_path):
    if model_name in ["vit", "tag-cnn"]:
        image_size = 224
    else:
        image_size = 299

    img = Image.open(image_path)
    img = img.resize((image_size, image_size))
    img = np.array(img)
    
    if model_name == "vit":
        X_vit = [img]
        X_vit = feature_extractor(images=X_vit, return_tensors="pt")["pixel_values"]
        X_vit = np.array(X_vit)
        X = X_vit

    return X
    