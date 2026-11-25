
import time
import torch
import whisper
import speech_recognition as sr
import tempfile
import os

device = "cuda" if torch.cuda.is_available() else "cpu"

print(f"Loading Whisper model on device: {device}")

load_start = time.time()
model = whisper.load_model("turbo", device=device)

print(f"Model loaded in {time.time() - load_start:.2f} seconds.")


def transcribe_file(audio_path):
    """
    Receives an audio file path and converts it to text using Whisper.
    """

    result = model.transcribe(
        audio_path,
        language="ar",
        fp16=(device == "cuda")
    )

    transcript_text = result["text"].strip()

    print(f"النص: {transcript_text}")

    return transcript_text


def Speech_to_text():
    """
    Records audio from the local microphone,
    saves it temporarily, then sends it to Whisper.
    """

    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 1.0

    mic = sr.Microphone()

    print("\nيمكنك التحدث الآن")

    try:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.3)
            print("جاري الاستماع...")
            audio = recognizer.listen(source)

        with tempfile.NamedTemporaryFile(
            suffix=".wav",
            delete=False
        ) as temp_audio:

            temp_audio.write(audio.get_wav_data())
            temp_audio_path = temp_audio.name

        try:
            print("Processing audio with Whisper...")
            return transcribe_file(temp_audio_path)

        finally:
            os.remove(temp_audio_path)

    except KeyboardInterrupt:
        print("\nExiting...")
        return None
