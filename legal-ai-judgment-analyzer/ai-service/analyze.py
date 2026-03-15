from flask import Flask, request, jsonify
import pdfplumber
import re

app = Flask(__name__)

def extract_text(file):

    text = ""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    return text


def extract_case_title(text):

    lines = text.split("\n")

    for line in lines[:10]:
        if "vs" in line.lower() or "v." in line.lower():
            return line.strip()

    return "Not Found"


def extract_judge(text):

    match = re.search(r"Justice\s+[A-Z][a-zA-Z]+", text)

    if match:
        return match.group()

    return "Not Found"


def extract_decision(text):

    keywords = ["allowed", "dismissed", "granted", "rejected"]

    for word in keywords:
        if word in text.lower():
            return word.capitalize()

    return "Not Found"


@app.route('/analyze', methods=['POST'])
def analyze():

    file = request.files['file']

    text = extract_text(file)

    case_title = extract_case_title(text)

    judge = extract_judge(text)

    decision = extract_decision(text)

    summary = text[:700]

    result = {
        "case_title": case_title,
        "judge": judge,
        "decision": decision,
        "summary": summary
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(port=5001)
