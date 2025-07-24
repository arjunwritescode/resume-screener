# 🧠 AI-Powered Resume Screener (FastAPI)

A lightweight backend application that intelligently screens resumes (PDFs) using AI and keyword analysis. Built using FastAPI and OpenAI, this tool extracts resume content, scores based on skill match, and generates an AI-driven evaluation.

---

## 📌 Features
- ✅ Upload resumes in PDF format.
- ✅ Extract text using PyMuPDF
- ✅ Basic skill-matching score (Python, SQL, ML, etc.)
- ✅ GPT-4 powered AI evaluation (verdict & skill summary)
- ✅ Simple frontend with HTML + JS for testing
- ✅ REST API docs via Swagger (`/docs`)

---

## 🚀 Tech Stack

| Layer      | Tech Used             |
|------------|-----------------------|
| Backend    | FastAPI, Uvicorn      |
| AI Model   | OpenAI (GPT-4 API)    |
| Parsing    | PyMuPDF               |
| Frontend   | Plain HTML + JS       |
| Env Mgmt   | python-dotenv         |

---

## 📂 Folder Structure

```
resume-screener/
│
├── main.py             # FastAPI app
├── requirements.txt    # Python deps
├── .env                # OpenAI API key (ignored)
├── index.html          # Simple frontend (local only)
├── venv/               # Python virtual environment
└── .gitignore          # Git ignore rules
```

---

## ⚙️ Local Setup

```bash
# Clone the repo
git clone https://github.com/yourusername/resume-screener.git
cd resume-screener

# Set up environment
python -m venv venv
.env\Scripts\Activate.ps1     # or source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Add your OpenAI API key
echo OPENAI_API_KEY=sk-xxxxx > .env

# Run the backend
uvicorn main:app --reload
```

---

## 🧪 Test the API

Go to: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
Try uploading a resume and view AI + skill match results.

---

## 🌐 Optional: Simple Frontend

Use `index.html` in your browser for a UI to upload and view results.

---

## 📈 What's Next?

- [ ] Add job description matching
- [ ] Export result as PDF
- [ ] Deploy backend to Render
- [ ] Deploy frontend to GitHub Pages
- [ ] Add logging and error reporting
- [ ] Save resume scoring history

---

## 🔐 Environment Variables

Make sure to create a `.env` file like:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

> ⚠️ `.env` is already included in `.gitignore`

---

## 🙋‍♂️ Author

Made with 💻 by [Arjun Rathore](https://github.com/yourusername)

---

## 📜 License

MIT License – use freely with credit.


