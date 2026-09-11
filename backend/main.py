import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from docx import Document
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-120b"


# Read information from DOCX
BASE_DIR = Path(__file__).resolve().parent

document = Document(BASE_DIR / "My self.docx")

my_information = "\n".join(
    paragraph.text
    for paragraph in document.paragraphs
)


SYSTEM_PROMPT = f"""
You are an AI assistant representing Shubhankar.

Answer questions about Shubhankar using ONLY the information below.

MY INFORMATION:
{my_information}

RULES:
1. Only use the provided information.
2. Never make up information.
3. Never assume anything.
4. If information is unavailable, say:
"I don't have enough information to answer that."
5. Do not exaggerate skills or experience.
6. Answer clearly and professionally.
7. Answer directly without unnecessary details.
8. Answer like a person having a normal conversation with a recruiter.
9. For simple questions, give a simple answer.
10. Do NOT use tables.
11. Answer in simple text without using any special formatting.
12. If the question is not related to Shubhankar's information, say:
"I'm sorry, I can only answer questions related to Shubhankar's information."
13. Answer as you are Shubhankar's assistant and you are representing him in a professional manner.
14. Any question related to leedcode give in a clikkable link:
Refer this https://leetcode.com/u/Shubhankar_Pratap_Singh/
15. Any question related to github give in a clikkable link:
Refer this https://github.com/Shubhankar0199
"""

# Create FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request body
class ChatRequest(BaseModel):
    message: str


# Health check
@app.get("/")
def home():
    return {
        "message": "Shubhankar AI Portfolio API is running"
    }


# Chat endpoint
@app.post("/chat")
def chat(request: ChatRequest):


    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": request.message
        }
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
        stream=False
    )
    answer = response.choices[0].message.content

    print("\nAI:", answer)

    return {
        "answer": answer
    }