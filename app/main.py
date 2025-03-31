from flask import Flask, send_from_directory, render_template
import os
import getpass
import config
from pathlib import Path

username = getpass.getuser()
VIDEO_FOLDER = config.SHAREFOLDER
app = Flask(__name__)

def get_video_structure(root_folder):
    video_structure = []
    
    for item in os.listdir(root_folder):
        item_path = os.path.join(root_folder, item)
        
        if os.path.isdir(item_path):
            folder_contents = []
            for subitem in os.listdir(item_path):
                if subitem.lower().endswith(('.mp4', '.avi', '.mkv', '.mov', '.webm')):
                    folder_contents.append({
                        "name": subitem,
                        "url": f"/videos/{item}/{subitem}"
                    })
            
            if folder_contents:
                video_structure.append({
                    "type": "folder",
                    "name": item,
                    "contents": folder_contents,
                    "count": len(folder_contents)
                })
        elif item.lower().endswith(('.mp4', '.avi', '.mkv', '.mov', '.webm')):
            video_structure.append({
                "type": "video",
                "name": item,
                "url": f"/videos/{item}"
            })
    
    return video_structure

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/videos")
def videos():
    video_structure = get_video_structure(VIDEO_FOLDER)
    return render_template("videos.html", video_structure=video_structure)

@app.route("/videos/<path:filename>")
def serve_video(filename):
    path = Path(VIDEO_FOLDER) / filename
    directory = str(path.parent)
    filename = path.name
    return send_from_directory(directory, filename)

if __name__ == "__main__":
    app.run("0.0.0.0", port=5005, debug=True)