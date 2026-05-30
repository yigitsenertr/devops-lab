from flask import Flask, render_template
import datetime
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', 
        time=datetime.datetime.now().strftime("%H:%M:%S"),
        env=os.getenv("APP_ENV", "development")
    )

@app.route('/health')
def health():
    return {"status": "ok"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
