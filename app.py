from flask import Flask, request, jsonify, render_template
import os
from werkzeug.utils import secure_filename
from cv_summurizee import extract_text_from_pdf, extract_text_from_docx, extract_text_from_txt, summarize_cv_with_deepseek
  # Add this line
app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'txt'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Extract text based on file type
        if filename.endswith('.pdf'):
            cv_text = extract_text_from_pdf(file_path)
        elif filename.endswith('.docx'):
            cv_text = extract_text_from_docx(file_path)
        elif filename.endswith('.txt'):
            cv_text = extract_text_from_txt(file_path)
        else:
            return jsonify({"error": "Unsupported file format"}), 400

        if cv_text:
            job_role = request.form.get('job_role', 'Full Stack Developer')
            check_similarity = request.form.get('check_similarity', 'false') == 'true'
            
            summary = summarize_cv_with_deepseek(
                cv_text, 
                job_role=job_role,
                calculate_similarity_flag=check_similarity
            )
            
            return jsonify({
                "summary": summary,
                "job_role": job_role
            })
        else:
            return jsonify({"error": "Failed to extract text from the file"}), 500

    return jsonify({"error": "File type not allowed"}), 400

if __name__ == '__main__':
    app.run(debug=True)