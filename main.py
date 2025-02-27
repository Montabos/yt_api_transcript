import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from youtube_transcript_api import YouTubeTranscriptApi

# Création de l'application FastAPI
app = FastAPI()

# Modèle pour recevoir l'entrée JSON
class VideoRequest(BaseModel):
    video_id: str

@app.get("/")
def home():
    return {"message": "API YouTube Transcript en ligne 🚀"}

@app.post("/get_transcript")
def get_transcript(request: VideoRequest):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(request.video_id, languages=['fr', 'en'])
        transcript_text = " ".join([t['text'] for t in transcript])
        return {"transcription": transcript_text}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Récupérer le port Railway
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
