import os
import glob
import webbrowser
from os.path import join, dirname, realpath
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from ocr_core import ocr_core #import OCR engine

CALL_FOLDER = "static/uploads/" #path from app.py
UPLOAD_FOLDER = join(dirname(realpath(__file__)), CALL_FOLDER) #path from /home...

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 #max file size of 1MB
app.config['UPLOAD_EXTENSIONS'] = ['png', 'jpg', 'jpeg'] #allowed extension

webbrowser.open('http://localhost:8081/', new=2)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['UPLOAD_EXTENSIONS'] # check uploaded file extension

# route and function to handle the home page
@app.route('/')
def home_page():
    return render_template('index.html')

# route and function to handle the upload page
@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        file = request.files['file']
        # if no file is selected
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')
        #if file is selected, check with allowable extension for valid file
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            folder_path = (os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.save(folder_path)
            #replace spacing on filename to underscore as it can causes err 404 in img_src
            new_filename = filename.replace(' ', '_')
            os.rename(folder_path,(os.path.join(app.config['UPLOAD_FOLDER'], new_filename)))
            # pass the image to OCR engine
            extracted_text = ocr_core(file)
            # pass the extracted text back to html.
            return render_template('upload.html',
                                   msg='Successfully processed',
                                   extracted_text=extracted_text,
                                   img_src=CALL_FOLDER + new_filename)
    elif request.method == 'GET':
        return render_template('upload.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)