from stt import Speech_to_text
from llm import ask_ai
from tts import Text_To_Speech


def main():
    while True:
        question = Speech_to_text()

        if not question:
            print("ارجع كرر كلامك ما سمعتك")
            continue

        print(f"السؤال: {question}")

        answer = ask_ai(question, 4)
        Text_To_Speech(response=answer)

        print(f"\n AI: {answer}\n")


if __name__ == "__main__":
    main()
