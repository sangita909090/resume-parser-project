Resume Parser Web Application (Streamlit)
This project is a Resume Parser Web Application built using Python and Streamlit.
It accepts a PDF resume, extracts key information, and displays the results in a web interface.

🚀 Features
Upload resume in PDF format

Extracts:

Candidate Name

Email Address

Phone Number

Skills

Built using Object-Oriented Programming (OOP)

Simple and interactive Streamlit UI

Deployed on Streamlit Cloud

🛠️ Technologies Used
Python

Streamlit

PyMuPDF (fitz) – PDF text extraction

spaCy – Named Entity Recognition

Regular Expressions (re) – Email & phone extraction

Git & GitHub – Version control

📂 Project Structure
resume-parser-project/
│
├── streamlit_app.py        # Streamlit frontend
├── resume_parser.py        # ResumeParser OOP class
├── requirements.txt        # Project dependencies
├── uploads/                # Temporary uploaded files
└── README.md               # Project documentation
⚙️ Installation & Run Locally
1️⃣ Clone the Repository
git clone https://github.com/sangita909090/resume-parser-project.git
cd resume-parser-project
2️⃣ Create Virtual Environment (Optional)
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm
4️⃣ Run Streamlit App
streamlit run streamlit_app.py
Open browser at:

http://localhost:8501
🌐 Live Demo
🔗 Live Application:
(Add your Streamlit Cloud link here once deployed)

📌 How It Works
User uploads a PDF resume

Resume text is extracted using PyMuPDF

Data is processed using NLP and Regex

Extracted information is displayed in JSON format

All logic follows OOP design principles

🎯 Future Enhancements
Skill matching with job roles

Resume ranking system

Export parsed data to CSV

Database integration (MySQL)

Job recommendation module
