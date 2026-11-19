from stt import Speech_to_text
from llm import ask_ai
from tts import Text_To_Speech
import time


def main():

    while True:

        question = Speech_to_text()

        if not question:
            print("ارجع كرر كلامك ما سمعتك")
            continue

        print(f"السؤال: {question}")

        answer = ask_ai(question, 4)

        if not answer:
            print("ما قدرت اجهزؤ إجابة")
            continue

        print(f"\nAI: {answer}\n")

        Text_To_Speech(response=answer)

        time.sleep(0.5)


if __name__ == "__main__":
    main()