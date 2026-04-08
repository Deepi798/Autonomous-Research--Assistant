from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.services.search_service import search_web
from app.services.scraper_service import extract_content
from app.services.llm_service import generate_report
from app.services.pdf_service import create_pdf

app = FastAPI()

# Enable CORS (frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend is running"}

@app.get("/research")
def research(topic: str):
    results = search_web(topic)

    sources = []
    for r in results:
        content = extract_content(r["url"])
        sources.append({
            "title": r["title"],
            "url": r["url"],
            "content": content
        })

    report = generate_report(topic, sources)
    pdf_file = create_pdf(report, sources)

    return {
        "topic": topic,
        "report": report,
        "sources": [
            {"title": s["title"], "url": s["url"]}
            for s in sources
        ],
        "pdf": pdf_file
    }