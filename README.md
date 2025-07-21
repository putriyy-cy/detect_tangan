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
```
---

## ⚙️ How to Run (Step-by-Step)
1. Clone the Repository
```bash
git clone https://github.com/yourusername/detect_tangan.git
cd detect_tangan
```
2. (Optional) Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```
3. Install Required Python Packages
```bash
pip install -r requirements.txt
```
4. Prepare YOLOv5 Model
- Place your trained model file (e.g., best.pt) into the yolov5/ directory.
- that detect.py is pointing to the correct path for the model.
5. Run the Flask App
```bash
python app.py
```
6. Open the Web Interface
Go to your browser and visit:
```cpp
http://127.0.0.1:5000
```
7. View & Save Results
- Detected frame is displayed in the browser.
- Captured output is saved automatically to the static/ folder.

---

## 🧠 Dataset & Model Info
- Dataset: Collected and labeled via Roboflow with hand annotations in YOLO format.
- Model: YOLOv5 custom-trained for hand detection tasks.
