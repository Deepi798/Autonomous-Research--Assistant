# Autonomous-Research--Assistant

The Autonomous Research Assistant is a simple AI-based web application that helps users generate structured research reports automatically. Instead of manually searching through multiple websites, this system collects information, summarizes it using AI, and presents it in a clean and readable format.

---

## 🚀 Overview

The user enters a research topic, and the system performs the following steps:

* Searches the internet for relevant sources
* Extracts useful content from those sources
* Uses an AI model to generate a structured report
* Displays the report along with source links
* Allows downloading the report as a PDF

This makes the research process faster and more efficient.

---

## 🧠 Technologies Used

* **Frontend:** React.js
* **Backend:** FastAPI (Python)
* **AI Model:** Groq (LLaMA 3.1)
* **Search API:** Tavily
* **Web Scraping:** Newspaper3k
* **PDF Generation:** ReportLab

---

## 📂 Project Structure

* `backend/` → FastAPI server, APIs, AI integration
* `frontend/` → React user interface
* `docs/` → Documentation files
* `docker/` → Deployment configuration
* `tests/` → Testing files

---

## ⚙️ How to Run the Project

### Backend Setup

```
cd backend
python -m venv venv
.\venv\Scripts\Activate
pip install -r requirements.txt
```

Create a `.env` file inside the backend folder:

```
GROQ_API_KEY=your_api_key
TAVILY_API_KEY=your_api_key
```

Run the backend server:

```
python -m uvicorn app.main:app --reload
```

---

### Frontend Setup

```
cd frontend
npm install
npm start
```

---

## 🌐 Usage

* Open the application in your browser
* Enter a research topic
* Click on **Search**
* View the generated report and sources
* Download the report as a PDF if needed

---

## ✨ Features

* AI-powered research generation
* Real-time web data collection
* Clean and simple user interface
* Research history tracking
* PDF export functionality

---

## 📌 Future Improvements

* Add citation numbering (like [1], [2])
* Chat with research feature
* Save reports for later use
* Improve formatting like research papers

---

## 🙌 Conclusion

This project shows how AI and modern web technologies can be combined to simplify the research process. It is useful for students and learners who want quick and structured information on any topic.
