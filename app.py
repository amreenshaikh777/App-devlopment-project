from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

notes = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        note_content = request.form.get('note')
        if note_content:
            new_note = {
                'timestamp': datetime.utcnow(),
                'content': note_content
            }
            notes.append(new_note)
            return redirect(url_for('home'))

    return render_template('home.html', notes=notes) 