from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from groq import Groq
import os
from dotenv import load_dotenv

from app.services.search_service import search_web
from app.services.scraper_service import extract_content
from app.services.llm_service import generate_report
from app.services.pdf_service import create_pdf

# Load environment variables
load_dotenv()

# Groq Client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# FastAPI App
app = FastAPI()

# Serve PDF folder
app.mount(
    "/files",
    StaticFiles(directory="generated_pdfs"),
    name="files"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Home Route
@app.get("/")
def home():

    return {
        "message": "Backend is running"
    }

# Research API
@app.get("/research")
def research(topic: str):

    try:

        # Search web
        results = search_web(topic)

        sources = []

        # Extract content
        for r in results:

            try:

                content = extract_content(
                    r["url"]
                )

                # Skip empty content
                if not content:
                    continue

                sources.append({
                    "title": r["title"],
                    "url": r["url"],
                    "content": content
                })

            except Exception as e:

                print("Skipping source:", e)
                continue

        # Fallback content
        if len(sources) == 0:

            sources.append({
                "title": "Wikipedia",
                "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
                "content": f"{topic} is an important topic in technology."
            })

        # Generate report
        report = generate_report(
            topic,
            sources
        )

        # Create PDF
        create_pdf(
            report,
            sources
        )

        return {

            "topic": topic,

            "report": report,

            "sources": [
                {
                    "title": s["title"],
                    "url": s["url"]
                }
                for s in sources
            ],

            "pdf":
            "http://127.0.0.1:8000/files/research_report.pdf"
        }

    except Exception as e:

        print("Main Error:", e)

        return {
            "topic": topic,
            "report": "Error generating report",
            "sources": [],
            "pdf": ""
        }

# Chat Request Model
class ChatRequest(BaseModel):
    report: str
    question: str

# Chat API
@app.post("/chat")
def chat(req: ChatRequest):

    try:

        prompt = f"""
        Research Report:
        {req.report}

        Answer this question:
        {req.question}
        """

        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.5,
            max_tokens=700
        )

        return {
            "answer":
            response.choices[0].message.content
        }

    except Exception as e:

        print("Chat Error:", e)

        return {
            "answer": "Error generating response"
        }