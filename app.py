from flask import Flask, render_template, send_from_directory
import os
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('index.html')

@app.route('/qr.jpg')
def qr():
    return send_from_directory('.', 'qr.jpg')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
