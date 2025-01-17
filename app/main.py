from flask import Flask, send_from_directory, render_template
import os
import getpass


username = getpass.getuser()

# Set the path to your video folder
VIDEO_FOLDER = f"/home/{username}/Videos/Hosting"  # Replace {username} with your actual username

app = Flask(__name__)

@app.route("/")
def index():
    # List available videos in the Hosting directory
    files = [
        {"name": video, "url": f"/videos/{video}"}
        for video in os.listdir(VIDEO_FOLDER)
        if video.lower().endswith(('.mp4', '.avi', '.mkv'))
    ]
    return render_template("index.html", files=files)

@app.route("/videos/<path:filename>")
def serve_video(filename):
    # Serve the video file from the specified directory
    return send_from_directory(VIDEO_FOLDER, filename)

if __name__ == "__main__":
    app.run("0.0.0.0" , port= 5005 , debug=True)
