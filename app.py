import tempfile
import os

from fastapi import FastAPI, UploadFile, File
from llm import ask_ai
from stt import transcribe_file

app = FastAPI()


@app.post("/ask")
def ask_question(audio: UploadFile = File(...)):

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
        temp_audio.write(audio.file.read())
        temp_audio_path = temp_audio.name

    try:
        question = transcribe_file(temp_audio_path)
        answer = ask_ai(question, 4)

        return {
            "question": question,
            "answer": answer
        }

    finally:
        os.remove(temp_audio_path)