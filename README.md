# test-app-chatgpt

This repository contains a tiny Flask web application that serves a page
showing the video stream from your 3D printer's AI camera.

## Setup

```bash
pip install -r requirements.txt
```

## Running

Set the environment variable `CAMERA_URL` to the URL of your camera's video
stream (defaults to `http://localhost:8000/stream`) and start the server:

```bash
export CAMERA_URL=http://your-printer/stream
python app.py
```

Then open `http://localhost:5000` in your browser. You can also override the
camera URL for a single request using the `url` query parameter:
`http://localhost:5000/?url=http://some/other/stream`.

## Docker

Build the container image:

```bash
docker build -t printer-camera-viewer .
```

Run the container, mapping the port and providing the camera stream URL:

```bash
docker run -p 5000:5000 -e CAMERA_URL=http://your-printer/stream printer-camera-viewer
```

After the container starts, visit `http://localhost:5000` in your browser to view the stream.
