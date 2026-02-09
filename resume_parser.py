import fitz
import re
import spacy

class ResumeParser:

    def __init__(self, file_path):
        self.file_path = file_path
        self.text = ""
        self.nlp = spacy.load("en_core_web_sm")

    def extract_text(self):
        doc = fitz.open(self.file_path)
        for page in doc:
            self.text += page.get_text()

    def extract_email(self):
        emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", self.text)
        return emails[0] if emails else None

    def extract_phone(self):
        phones = re.findall(r"\b\d{10}\b", self.text)
        return phones[0] if phones else None

    def extract_name(self):
        doc = self.nlp(self.text)
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                return ent.text
        return None

    def extract_skills(self):
        skills = ["python","java","sql","html","css","javascript","machine learning"]
        found = []
        for s in skills:
            if s.lower() in self.text.lower():
                found.append(s)
        return found

    def parse_resume(self):
        self.extract_text()
        return {
            "name": self.extract_name(),
            "email": self.extract_email(),
            "phone": self.extract_phone(),
            "skills": self.extract_skills()
        }
