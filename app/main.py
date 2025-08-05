from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'visitors.db')

def init_db():
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS visits (count INTEGER)')
        c.execute('INSERT INTO visits (count) VALUES (0)')
        conn.commit()
        conn.close()

@app.route('/')
def home():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('UPDATE visits SET count = count + 1')
    conn.commit()
    c.execute('SELECT count FROM visits')
    count = c.fetchone()[0]
    conn.close()
    return render_template('index.html', count=count)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
