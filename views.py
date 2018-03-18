import os

from flask import request, jsonify
from werkzeug.utils import secure_filename

from app import app


@app.route('/')
def index():
    return '<h1>test</h1>'


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if not os.path.exists('UPLOAD_FOLDER'):
        os.makedirs('UPLOAD_FOLDER')

    if request.method == 'POST':
        uploadfile = request.files['file']
        uploadfile.save(os.path.join('UPLOAD_FOLDER', secure_filename(uploadfile.filename)))

    return jsonify({'message': 'upload completed!'})
