from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS visits (count INTEGER)')
    cursor.execute('SELECT count FROM visits')
    row = cursor.fetchone()
    count = row[0] + 1 if row else 1
    cursor.execute('DELETE FROM visits')
    cursor.execute('INSERT INTO visits (count) VALUES (?)', (count,))
    conn.commit()
    conn.close()
    return render_template('index.html', count=count)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
