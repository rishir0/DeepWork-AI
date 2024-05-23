from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Set the directory for storing data
DATA_DIR = r'/Users/rayhanmohammad/Desktop/rishiravi/C:\Users\draco\OneDrive\Desktop\DeepWork AI\data'

# Create the data directory if it doesn't exist
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

@app.route('/')
def index():
    files = os.listdir(DATA_DIR)
    return render_template('/Users/rayhanmohammad/Desktop/rishiravi/templates/index.html', files=files)

@app.route('/view/<filename>')
def view_file(filename):
    filepath = os.path.join(DATA_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            content = file.read()
        return render_template('view.html', filename=filename, content=content)
    else:
        return "File not found"

@app.route('/delete/<filename>')
def delete_file(filename):
    filepath = os.path.join(DATA_DIR, filename)
    if os.path.exists(filepath):
        os.remove(filepath)
        return redirect(url_for('index'))
    else:
        return "File not found"

@app.route('/save_data', methods=['POST'])
def save_data():
    data = request.form['data']
    filename = request.form['filename']
    filepath = os.path.join(DATA_DIR, filename)

    with open(filepath, 'w') as file:
        file.write(data)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
