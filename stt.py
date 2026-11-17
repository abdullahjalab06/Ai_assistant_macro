import time
import torch
import whisper
import speech_recognition as sr

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f" Loading Whisper model on device: {device}")

load_start = time.time()
model = whisper.load_model("turbo", device=device)
print(f"Model loaded in {time.time() - load_start:.2f} seconds.")


def Speech_to_text():
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 1.0  # تقليص وقت الانتظار قليلاً لسرعة الاستجابة
    
    mic = sr.Microphone()

    print("\nيمكنك التحدث الان")

    try:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.3)
            print(" جاري الاستماع...")
            audio = recognizer.listen(source)

        # حفظ الصوت المؤقت
        with open("temp.wav", "wb") as f:
            f.write(audio.get_wav_data())

        print(" Processing & Transcribing on GPU...")
        
        # بدء قياس وقت التفريغ الصوتي
        start_time = time.time()
        
        result = model.transcribe(
            "temp.wav", 
            language="ar", 
            fp16=(device == "cuda")
        )
        
        end_time = time.time()
        elapsed_time = end_time - start_time

        transcript_text = result["text"].strip()

        print(f" النص: {transcript_text}")

        return transcript_text

    except KeyboardInterrupt:
        print("\nExiting...")
        return None

#if __name__ == "__main__":
# Speech_to_text()