Resumate-AI

Short tagline: AI Resume Analyzer — ATS scoring, skill extraction, interview practice & analytics.

Project overview

Resumate-AI analyzes uploaded resumes (PDF), extracts skills, predicts a career field, provides ATS-style scoring, gives improvement suggestions and offers AI-driven mock interview sessions and analytics dashboards.

Key features

Resume PDF upload + extraction (pdfminer).

Skill extraction + ATS scoring and recommendations.

Career field prediction (Naive Bayes TF-IDF).

AI-backed interview practice and automated scoring fallback.

Clustering analytics (K-Means) to categorize users by resume quality.

Job search helper via RapidAPI (job fetch) and YouTube learning links.
(Implementation details and code references in the app2.py file.) 



Tech stack

Python (3.10+ recommended)

Streamlit (UI) — main app: app2.py. 

ML: scikit-learn (TF-IDF, Naive Bayes, KMeans), nltk

PDF parsing: pdfminer.six

Optional APIs: GROQ (LLM call points), RapidAPI job search

Visualization: Plotly

Storage: local CSV (demo) — resumate_data/ (users.csv, feedback.csv, interviews.csv)

See requirements.txt for full versions. 

requirements

Architecture (high level)

See ARCHITECTURE.md for a diagram (Mermaid included). Core components:

Streamlit frontend (app2.py) — handles uploads, UI, and orchestration. 



ML modules — TF-IDF & NB for field prediction, clustering for analytics.

CSV persistence (resumate_data/) for demo.

External integrations: GROQ and RapidAPI (configurable via env vars).




Setup & Run (local demo)

Clone repo or download zip.

Create a virtual env and activate:

python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows


Install dependencies:

pip install -r requirements.txt


Create .env from .env.example, fill real keys (if you have them).

Run the Streamlit app:

export STREAMLIT_SERVER_HEADLESS=true
streamlit run app2.py


Then open http://localhost:8501.
