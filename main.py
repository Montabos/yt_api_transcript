from fastapi import FastAPI, HTTPException
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API YouTube Transcript en ligne 🚀"}

@app.get("/transcript/{video_id}")
def get_transcript(video_id: str):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = " ".join([entry['text'] for entry in transcript])  # Récupérer uniquement le texte
        return {"video_id": video_id, "transcript": text}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erreur : {str(e)}")

