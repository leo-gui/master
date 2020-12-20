from flask import Flask
from flask import request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory
from pypinyin import lazy_pinyin
import os
app = Flask(__name__)
UPLOAD_FOLDER = "/Users/guiyang/Documents/test/"
ALLOW_EXTENTION = ['txt', 'jpg', 'pdf', 'png', 'doc', 'docx']

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allow_filename(filename):
    return "." in filename \
            and filename.split('.')[1] in ALLOW_EXTENTION


@app.route('/upload/file', methods=['POST', 'GET'])
def upload_file():
    if request.method == "POST":
        file = request.files['file']
        if file and allow_filename(file.filename):
            new_filename = '_'.join(lazy_pinyin(file.filename.split('.')[0]))
            filename = secure_filename(new_filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for("uploaded_file", filename=filename))
        else:
            return "<h1>该文件类型不支持</h1>"
    return '''
        <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
           '''


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == "__main__":
    app.run(port=8080)
