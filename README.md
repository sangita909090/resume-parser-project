Resume Parser System
This project is a simple Resume Parser web application built using Python and Streamlit.
It allows users to upload a PDF resume and automatically extracts useful details such as name, email, phone number, and skills. The main goal of this project is to understand how PDF parsing, basic NLP, and Object-Oriented Programming can be used together in a real application.

Live Demo
(Link will be added after deployment)
https://resume-parser.streamlit.app

What this project can do
Upload a resume in PDF format

Extract candidate name

Extract email address and phone number

Identify basic technical skills

Show results instantly on screen

Tools and Technologies
Python

Streamlit

PyMuPDF (fitz)

spaCy

Regular Expressions (re)

Project Files
resume-parser-project/
│
├── streamlit_app.py    # Main Streamlit app
├── resume_parser.py   # Resume parsing logic
├── requirements.txt   # Libraries used
└── uploads/            # Temporary uploaded resumes
How to run this project on your system
Install all required libraries:

pip install -r requirements.txt
python -m spacy download en_core_web_sm
Start the application:

streamlit run streamlit_app.py
Open your browser and go to:

http://localhost:8501
Upload a PDF resume and view the extracted details.

How it works
The resume PDF is read using PyMuPDF

Text is processed using spaCy and regex

A Python class handles all extraction logic

Streamlit displays the output in a simple web interface

Future Improvements
Add more skill categories

Improve accuracy of name detection

Save parsed data to a database

Add job role matching
