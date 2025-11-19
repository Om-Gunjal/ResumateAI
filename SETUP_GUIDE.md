# Setup Guide (local)

1) Prepare venv
python -m venv venv
# activate venv
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate

2) Install deps
pip install -r requirements.txt

3) Prepare environment
cp .env.example .env
# Edit .env and add your GROQ_API_KEY and RAPIDAPI_KEY if needed

4) Run app (Streamlit)
streamlit run app2.py

5) Access UI
Open http://localhost:8501
