import os
import uuid

import qrcode
from flask import Flask, render_template, request, send_file

QRCODE_FOLDER = os.path.join('qrcodes')
STATIC_FOLDER = os.path.join('static')

app = Flask(__name__)
app.config['QRCODE_FOLDER'] = QRCODE_FOLDER
app.config['STATIC'] = STATIC_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.form['data']
    qr = qrcode.make(data)
    qr_file = "{}.png".format(str(uuid.uuid4()))
    qr.save(os.path.join(app.root_path, app.config['STATIC'], app.config['QRCODE_FOLDER'], qr_file))
    
    full_filename = os.path.join(app.config['STATIC'], app.config['QRCODE_FOLDER'], qr_file)
    return render_template("index.html", qrcode = full_filename)


if __name__ == '__main__':
    app.run(debug=True)
