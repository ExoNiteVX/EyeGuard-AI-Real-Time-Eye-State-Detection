# 👁️ EyeGuard AI – Real-Time Eye State Detection

EyeGuard AI is a Python-based real-time eye state detection system using OpenCV and MediaPipe. It identifies whether your eyes are open or closed using facial landmarks from your webcam feed.

---

## 🚀 Features

- Real-time webcam processing
- Eye open/closed detection using face landmarks
- Visual feedback on screen
- Lightweight and fast

---

## 🧠 How It Works

The system tracks facial landmarks using MediaPipe Face Mesh and calculates the vertical distance between two key eye points:

- Landmark 159 → Upper eyelid
- Landmark 145 → Lower eyelid

If the distance is below a threshold, the eye is considered **closed**; otherwise, **open**.

---

## 🛠️ Requirements

- Python 3.x
- OpenCV
- MediaPipe
- NumPy

Install dependencies:
```bash
pip install opencv-python mediapipe numpy

Press Q to quit the application.

🧪 Example Output

🟢 "Eyes opened" → Eyes are open

🔴 "Eyes closed" → Eyes are closed

🔮 Future Improvements

Blink counting

Drowsiness scoring

Multi-face tracking

Eye fatigue estimation




📜 License

This project is open-source and free to use for learning and experimentation.
