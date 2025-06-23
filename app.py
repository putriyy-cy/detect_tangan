
from flask import Flask, render_template, Response
import cv2
import torch
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

app = Flask(__name__)

# Load YOLOv5 model sekali saja
model = torch.hub.load(
    'yolov5', 
    'custom', 
    path='yolov5/best.pt',  # path relatif ke app.py
    source='local',
    force_reload=True  # untuk memastikan tidak ambil cache lama
)

# Buka kamera
cap = cv2.VideoCapture(0)

def gen_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            # YOLO deteksi
            results = model(frame)

            # Render hasil ke frame
            annotated_frame = results.render()[0]

            # Encode ke jpeg
            ret, buffer = cv2.imencode('.jpg', annotated_frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)