# 👁️ EyeGuard AI
### *Real-Time Biometric Vision for Fatigue & Drowsiness Monitoring*

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.5+-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Latest-00C7B7?style=for-the-badge&logo=google&logoColor=white)](https://mediapipe.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=for-the-badge)](https://github.com/)

**EyeGuard AI** is a high-performance computer vision pipeline designed to monitor ocular states in real-time. By leveraging the **MediaPipe Face Mesh** (468+ landmarks), EyeGuard precisely calculates eye-aspect ratios to detect fatigue, blinks, and prolonged closure, making it an ideal foundation for driver safety systems or productivity trackers.

---

## ✨ Key Features

* **⚡ Sub-10ms Inference:** Optimized for real-time processing even on CPU-only machines.
* **🎯 High Precision:** Utilizes the Eye Aspect Ratio (EAR) algorithm for robust detection.
* **📊 Live HUD:** On-screen visual indicators with dynamic status labeling (Open/Closed).
* **📈 Adaptive Thresholds:** Designed to handle varying lighting conditions and facial structures.
* **🛠️ Developer Friendly:** Clean, modular Python code ready for integration into IoT or safety projects.

---

## 🧠 The Science: How It Works

The system doesn't just "look" for eyes; it measures the geometry of the eyelid. We track the Euclidean distance between specific vertical landmarks relative to horizontal ones. 

The core logic uses the **Eye Aspect Ratio (EAR)**. For a specific eye, the ratio is calculated as:

$$EAR = \frac{||P_2 - P_6|| + ||P_3 - P_5||}{2 ||P_1 - P_4||}$$

| Landmark Feature | MediaPipe ID |
| :--- | :--- |
| **Upper Eyelid** | 159 |
| **Lower Eyelid** | 145 |
| **Inner Corner** | 33 |
| **Outer Corner** | 133 |

---

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/yourusername/EyeGuard-AI.git](https://github.com/yourusername/EyeGuard-AI.git)
cd EyeGuard-AI
2. Create a Virtual Environment (Recommended)
Bash
python -m venv venv
# On Windows:
venv\Scripts\activate 
# On Mac/Linux:
source venv/bin/activate
3. Install Dependencies
Bash
pip install opencv-python mediapipe numpy
🚀 Usage
Run the main detection script:

Bash
python main.py
Controls
Q: Safely exit the application and release the webcam.

S: (Coming Soon) Save a screenshot of the current frame.


🔮 Roadmap
[ ] Drowsiness Alarm: Trigger an audio alert if eyes are closed for >2 seconds.

[ ] Blink Rate Analytics: Track blinks per minute (BPM) to estimate eye strain.

[ ] Gaze Tracking: Determine where the user is looking on the screen.

[ ] Dark Mode Support: Optimization for IR-based cameras.


🤝 Contributing
Fork the Project.

Create your Feature Branch (git checkout -b feature/AmazingFeature).

Commit your Changes (git commit -m 'Add some AmazingFeature').

Push to the Branch (git push origin feature/AmazingFeature).

Open a Pull Request.

📜 License
Distributed under the MIT License. See LICENSE for more information.


Developed with ❤️ by ExoNiteVX

