# ✋ Real-Time Hand Detection System using YOLOv5 & Flask

Created by **Putri Yuliana Chairiah Azmi**  
*(Politeknik Caltex Riau)*

This project is a real-time hand detection system powered by YOLOv5 and live camera input. It uses Flask as the web framework to stream the detection output directly to a browser. Suitable for gesture-based interaction systems, touchless control, or security applications.

---

## 🚀 Key Features

- 🔍 **Real-Time Hand Detection**  
  Utilizes a custom-trained YOLOv5 model for fast and accurate hand detection.

- 📸 **Capture and Save Output**  
  Automatically saves the detection image into the `static/` folder.

---

## 🛠 Technologies Used

| Technology | Description |
|------------|-------------|
| Python 3.x | Main programming language |
| YOLOv5     | Object detection model |
| Flask      | Lightweight web framework |
| OpenCV     | Real-time image and video processing |
| PyTorch    | Deep learning library (used by YOLOv5) |

---

## 📁 Project Structure

```bash
.
├── app.py                # Main Flask application
├── detect.py             # YOLOv5 detection logic
├── yolov5/               # YOLOv5 custom model directory
├── static/
│   └── result.jpg        # Output detection image
├── templates/
│   └── index.html        # Front-end web interface
└── requirements.txt      # Python dependencies
