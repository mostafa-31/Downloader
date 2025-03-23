from flask import Flask, request, jsonify
import yt_dlp
import os
import subprocess  # For opening file location
from datetime import datetime  # Import for timestamp

app = Flask(__name__)

DOWNLOAD_DIR = os.path.expanduser("~/Downloads")
# DOWNLOAD_DIR = "C:/Users/Utshab/Videos"


@app.route("/formats", methods=["GET"])
def get_formats():
    url = request.args.get("url")
    if not url:
        return jsonify({"success": False, "error": "No URL provided"})

    try:
        with yt_dlp.YoutubeDL({"quiet": True}) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = [
                {
                    "format_id": f["format_id"],
                    "resolution": f.get("resolution", "Unknown"),
                    "ext": f["ext"],
                }
                for f in info.get("formats", [])
            ]
        return jsonify({"success": True, "formats": formats})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


@app.route("/download", methods=["POST"])
def download_video():
    data = request.json
    url = data.get("url")
    format_id = data.get("format")

    if not url or not format_id:
        return jsonify({"success": False, "error": "Missing parameters"})

    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        ydl_opts = {
            "format": format_id,
            "outtmpl": os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s"),
            "quiet": False,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)  # Downloading video
            file_name = ydl.prepare_filename(info_dict)  # Get downloaded file name

        # Open file location with the downloaded file selected
        if os.name == "nt":  # Windows
            subprocess.run(
                ["explorer", "/select,", file_name]
            )  # Opens File Explorer with file selected
        else:  # macOS/Linux
            subprocess.run(["xdg-open", DOWNLOAD_DIR])  # Opens Downloads folder

        return jsonify(
            {"success": True, "message": "Download completed!", "path": file_name}
        )
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
