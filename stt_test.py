import asyncio
import edge_tts


async def main():

    text = "أهلاً وسهلاً بكم في شركة ماكروليد. كيف يمكنني مساعدتكم اليوم؟"

    communicate = edge_tts.Communicate(
        text=text,
        voice="ar-SA-HamedNeural",
        rate="+15%"
    )

    await communicate.save("test_voice.mp3")

    print("تم إنشاء الملف الصوتي")


asyncio.run(main())

import speech_recognition as sr
import whisper

print("Loading model...")
model = whisper.load_model("medium")


def Speech_to_text():

    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("🎤 Ready for listening...")

    try:
        with mic as source:

            recognizer.adjust_for_ambient_noise(source)

            print(" Listening...")

            audio = recognizer.listen(
                source,
                phrase_time_limit=20
            )

        # Save recorded audio
        with open("temp.wav", "wb") as f:
            f.write(audio.get_wav_data())

        # Convert speech to text
        result = model.transcribe("temp.wav")

        transcript_text = result["text"].strip()

        print(f"💬 {transcript_text}")

        return transcript_text

    except KeyboardInterrupt:
        print("\nExiting...")
        return None