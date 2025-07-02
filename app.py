from flask import Flask, render_template, Response, request
import cv2
import torch
import os
import pathlib

# Patch agar PosixPath bekerja di Windows
pathlib.PosixPath = pathlib.WindowsPath

app = Flask(__name__)

# Load model YOLOv5
model = torch.hub.load(
    'yolov5',
    'custom',
    path='yolov5/best.pt',
    source='local'
)

# Buat folder statis jika belum ada
os.makedirs('static', exist_ok=True)

# Inisialisasi kamera
cap = cv2.VideoCapture(0)

# Fungsi untuk streaming dari webcam
def gen_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            results = model(frame)
            annotated_frame = results.render()[0]
            ret, buffer = cv2.imencode('.jpg', annotated_frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html', result_img=False)

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return "No file part", 400
    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400

    image_path = os.path.join('static', 'uploaded.jpg')
    file.save(image_path)

    # Jalankan deteksi YOLO
    results = model(image_path)
    results.render()
    annotated_img = results.ims[0]
    result_path = os.path.join('static', 'result.jpg')
    cv2.imwrite(result_path, annotated_img)

    return render_template('index.html', result_img=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
