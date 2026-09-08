# 📄 CV Summarizer

A web application that automatically **analyzes and summarizes CVs** using Python.
The application allows users to upload a CV and obtain a concise summary of its content through an easy-to-use web interface.

##  Project Overview

The **CV Summarizer** project aims to simplify the analysis of resumes by automatically extracting and summarizing relevant information from a CV.

Instead of manually reviewing a long resume, the application provides a structured and concise overview of the candidate's profile.

### Main objectives

*  Upload and process CVs
*  Extract relevant information
*  Automatically summarize CV content
*  Provide results through a simple web interface
*  Deploy the application as a web application

##  Features

* CV upload functionality
* Automated CV processing
* Automatic text summarization
* Simple and user-friendly interface
* Web-based application
* Python backend
* HTML templates for the user interface

##  Project Architecture

```text
cv_summurize/
│
├── templates/
│   └── ...                 # HTML templates
│
├── app.py                 # Main web application
├── cv_summurizee.py       # CV processing and summarization
├── requirements.txt       # Python dependencies
├── .gitignore
└── README.md
```

## How It Works

The application follows a simple workflow:

```text
        ┌──────────────┐
        │  Upload CV   │
        └──────┬───────┘
               │
               ▼
        ┌──────────────┐
        │ Extract Text │
        └──────┬───────┘
               │
               ▼
        ┌──────────────┐
        │ Process CV   │
        └──────┬───────┘
               │
               ▼
        ┌──────────────┐
        │  Summarize   │
        └──────┬───────┘
               │
               ▼
        ┌──────────────┐
        │ Display      │
        │ Summary      │
        └──────────────┘
```

## 🛠️ Technologies

* **Python**
* **Flask**
* **HTML / CSS**
* **Natural Language Processing (NLP)**
* **Text Processing**
* **PythonAnywhere** for deployment

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/hebaabbadi/cv_summurize.git
cd cv_summurize
```

### 2. Create a virtual environment

It is recommended to use a dedicated Python virtual environment.

```bash
python -m venv .venv
```

### 3. Activate the environment

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### 4. Configure the environment in VS Code

If you are using VS Code:

1. Open the project folder.
2. Press `Cmd + Shift + P` on macOS or `Ctrl + Shift + P` on Windows.
3. Select **Python: Select Interpreter**.
4. Select the Python interpreter from `.venv`.

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

##  Run the Application

Start the Flask application with:

```bash
python app.py
```

The application will then be available locally through the address displayed in the terminal.

##  Deployment

The application was also deployed using **PythonAnywhere**, allowing the CV summarization application to be accessed as a web application.

##  Skills Demonstrated

This project demonstrates practical experience in:

* Python development
* Web application development
* Natural Language Processing
* Text extraction and processing
* Automated summarization
* Flask
* Frontend/backend integration
* Web deployment

##  Future Improvements

Possible improvements include:

* Support for additional CV formats
* More advanced NLP models
* Structured extraction of:

  * Skills
  * Education
  * Experience
  * Certifications
  * Languages
* Candidate/job matching
* CV scoring
* Keyword and ATS analysis
* Multilingual CV summarization
* Integration with modern Transformer-based NLP models

##  Author

**Hiba Abbadi**

AI Engineering | Machine Learning | NLP | Full-Stack Development

---

⭐ If you find this project useful, feel free to explore the repository and experiment with the application.
