import os
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "defaultsecretkey")
db_url = os.getenv("DATABASE_URL")

counter = 0

@app.route('/')
def home():
    global counter
    counter += 1
    return render_template('index.html', count=counter)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
