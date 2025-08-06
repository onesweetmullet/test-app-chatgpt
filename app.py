import os
from flask import Flask, render_template, request

app = Flask(__name__)

# Default camera URL can be overridden with an environment variable
DEFAULT_CAMERA_URL = os.environ.get('CAMERA_URL', 'http://localhost:8000/stream')

@app.route('/')
def index():
    """Render page showing the camera stream.

    A query parameter `url` can be used to override the camera URL
    at request time.
    """
    camera_url = request.args.get('url', DEFAULT_CAMERA_URL)
    return render_template('index.html', camera_url=camera_url)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
