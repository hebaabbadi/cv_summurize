from langdetect import detect
from openai import OpenAI
import PyPDF2
import logging
from docx import Document
import re
import os
from difflib import SequenceMatcher
# Initialize OpenAI client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",  # Replace with your OpenRouter API key
)


def clean_text(text):
    """Clean and normalize the extracted text."""
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() if page.extract_text() else ""
            logging.info("Text extracted successfully from PDF.")
            return clean_text(text)
    except Exception as e:
        logging.error(f"Error reading PDF file: {e}")
        return None

def extract_text_from_docx(docx_path):
    """Extract text from a DOCX file."""
    try:
        doc = Document(docx_path)
        text = "\n".join([para.text for para in doc.paragraphs])
        logging.info("Text extracted successfully from DOCX.")
        return clean_text(text)
    except Exception as e:
        logging.error(f"Error reading DOCX file: {e}")
        return None

def extract_text_from_txt(txt_path):
    """Extract text from a TXT file."""
    try:
        with open(txt_path, "r", encoding='utf-8') as file:
            text = file.read()
        logging.info("Text extracted successfully from TXT.")
        return clean_text(text)
    except Exception as e:
        logging.error(f"Error reading TXT file: {e}")
        return None

def detect_language(text):
    """Detect the language of the text."""
    try:
        return detect(text)
    except:
        return "en"



def summarize_cv_with_deepseek(cv_text, job_role="Full Stack Developer", calculate_similarity_flag=False):
    """Summarize a CV using DeepSeek model."""
    language = detect_language(cv_text)

    if language == "fr":
        prompt = f"""
        Analysez le CV suivant et fournissez un résumé structuré et concis en français pour le poste de {job_role}:
        - Nom et coordonnées
        - Compétences techniques pertinentes
        - Expérience professionnelle pertinente
        - Formation et diplômes pertinents
        - Langues
        - Autres informations pertinentes

        CV:
        {cv_text}

        Résumé structuré:
        """
    else:
        prompt = f"""
        Analyze the following CV and provide a structured and concise summary in English for the {job_role} position:
        - Name and contact information
        - Relevant technical skills
        - Relevant professional experience
        - Relevant education and degrees
        - Languages
        - Other relevant information

        CV:
        {cv_text}

        Structured Summary:
        """

    completion = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",
        messages=[{"role": "user", "content": prompt}]
    )

    summary = completion.choices[0].message.content
    
    if calculate_similarity_flag:
        similarity_score = calculate_similarity(cv_text, job_role)
        summary = f"{summary}\n\n=== Similarity Assessment ===\nRelevance to '{job_role}': {similarity_score}%"
    
    return summary
def calculate_similarity(cv_text, job_role):
    """
    Universal job similarity using DeepSeek's AI understanding
    - Works for ALL professions (tech, business, healthcare, etc.)
    - No hardcoded keywords
    - Dynamic relevance assessment
    """
    # Use DeepSeek to analyze match quality
    prompt = f"""
    Analyze how well this CV matches the job role "{job_role}".
    Consider:
    1. Required skills/qualifications
    2. Industry terminology
    3. Experience relevance
    4. Education alignment

    Return ONLY a percentage (0-100) representing match quality.

    CV:
    {cv_text[:3000]}  # Truncate to avoid token limits

    Percentage: """
    
    response = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1  # Keep outputs precise
    )
    
    # Extract numeric value from response
    try:
        return float(re.search(r'\d+', response.choices[0].message.content).group())
    except:
        return 50.0  # Default if parsing fails

def save_summary_to_file(summary, output_path="summary.txt"):
    """Save the summary to a text file."""
    try:
        with open(output_path, "w", encoding='utf-8') as file:
            file.write(summary)
        logging.info(f"Summary saved to {output_path}")
        return True
    except Exception as e:
        logging.error(f"Error saving summary to file: {e}")
        return False