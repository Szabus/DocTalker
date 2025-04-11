# Text-to-Speech Web API

This is a simple FastAPI-based backend application that provides a text-to-speech service via HTTP. The service receives a piece of text and responds with a generated `.mp3` file using the gTTS (Google Text-to-Speech) library.

## Features

- FastAPI backend
- POST endpoint `/speak` that returns an audio file
- Language selection support (e.g., `hu`, `en`, `de`)
- CORS enabled for frontend integration

## Getting Started

### Installation

```bash
git clone https://github.com/yourusername/tts-backend.git
cd tts-backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
