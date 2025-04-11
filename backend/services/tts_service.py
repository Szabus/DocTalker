from gtts import gTTS
import tempfile


def text_to_speech(text: str, lang: str = "hu") -> str:
    tts = gTTS(text, lang=lang)
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(tmp.name)
    return tmp.name
