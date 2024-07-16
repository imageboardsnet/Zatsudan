from flask import Flask, render_template, send_from_directory
import os
import json
from zutils import timestamp_to_humane

app = Flask(__name__)

app.jinja_env.filters['humane_date'] = timestamp_to_humane

def render_page(content):
    return render_template('index.html', content=content)

def get_messages():
    with open('data/zatsudan.json', 'r') as f:
        return json.load(f)

@app.route('/')
def root():
    messages = get_messages()
    content = render_template('chat.html', messages=messages)
    return render_page(content)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run() 

def create_app():
    return app
