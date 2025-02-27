from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
import os

app = Flask(__name__)

@app.route("/get_transcript", methods=["POST"])
def get_transcript():
    data = request.json
    video_id = data.get("video_id")

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['fr', 'en'])
        transcript_text = " ".join([t['text'] for t in transcript])
        return jsonify({"transcription": transcript_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Utilise le port Railway
    app.run(host="0.0.0.0", port=port)
