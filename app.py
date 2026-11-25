from fastapi import FastAPI
from pydantic import BaseModel
from llm import ask_ai
from stt import Speech_to_text


app = FastAPI()



@app.post("/ask")
def ask_question(question):
    question = Speech_to_text()
    answer = ask_ai(question, 4)

    return {
        "question" : question,
        "answer": answer

    }