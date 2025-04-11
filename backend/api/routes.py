from fastapi import APIRouter, Request
from fastapi.responses import FileResponse
from backend.services.tts_service import text_to_speech

router = APIRouter()


@router.post("/speak")
async def speak_text(request: Request):
    data = await request.json()
    text = data.get("text")
    lang = data.get("lang", "hu")
    if not text:
        return {"error": "No text provided"}

    audio_path = text_to_speech(text, lang)
    return FileResponse(audio_path, media_type="audio/mpeg")
