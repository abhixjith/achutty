from flask import Flask, send_from_directory
import os
import random
app = Flask(__name__)


IMAGE_FOLDER = "IMG_DB"  
@app.route("/")
def index():    
    return "Alive"




@app.route("/Anime-girl")
def random_image():
    images = [f for f in os.listdir(IMAGE_FOLDER) if f.endswith((".png", ".jpg", ".jpeg", ".gif"))]
    if not images:
        return "No images found", 404
    random_image = random.choice(images)
    return send_from_directory(IMAGE_FOLDER, random_image)




if __name__ == "__main__":
    app.run()