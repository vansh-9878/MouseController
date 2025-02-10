# Hand Tracking Mouse Controller

Control your mouse cursor using hand gestures with a webcam! This project utilizes **OpenCV, MediaPipe, and PyAutoGUI** to detect hand landmarks and translate finger movements into mouse actions.

## ✨ Features
- 🎥 **Real-time Hand Tracking** – Uses **MediaPipe Hands** for accurate hand landmark detection.
- 🖱️ **Mouse Cursor Control** – Move your index finger to control the mouse pointer.
- 👆 **Click with a Pinch** – Bringing your thumb and index finger close together simulates a mouse click.

## 📌 Requirements
Make sure you have the following installed:
- Python 3.x
- OpenCV (`cv2`)
- NumPy
- PyAutoGUI
- MediaPipe

### Install dependencies:
```bash
pip install opencv-python numpy pyautogui mediapipe
```

## 🚀 How to Run
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/hand-tracking-mouse.git
   cd hand-tracking-mouse
   ```
2. **Run the script**
   ```bash
   python handMouseControl.py
   ```
3. **Use your hand to move the cursor!**
   - Move your **index finger** to control the mouse.
   - Bring your **thumb and index finger close together** to click.


## 🤖 Future Improvements
- ✋ Add gesture-based scrolling and dragging.
- 📌 Improve accuracy with Kalman filtering.
- 🖥️ Support multiple monitors.


## 📝 License
This project is **open-source** and available under the **GNU License**.

---
💡 *Pull requests and feature suggestions are welcome!* 🚀

