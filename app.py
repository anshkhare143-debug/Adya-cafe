from flask import Flask, render_template, send_from_directory
import os
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('index.html')

@app.route('/IMG-20261022-WA0015.jpg')
def qr():
    return send_from_directory('.', 'IMG-20261022-WA0015.jpg')

@app.route('/qr.jpg')
def qr2():
    return send_from_directory('.', 'IMG-20261022-WA0015.jpg')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
