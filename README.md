## Author: Shashank Hegde
## Institute: Moodlakatte Institute Of Technology, Kundapuara

# Real-Time Yawn Detector

An intelligent, real-time computer vision application designed to monitor facial geometry and detect when a user is yawning. It processes video data instantly from your webcam, tracks micro-landmarks around the inner lips, and triggers an overlay warning when facial ratios indicate drowsiness.

---

## Features
* **Zero-dlib Configuration:** Bypasses heavy C++ compiler packages and custom `.dat` training assets using Google's ultra-lightweight MediaPipe infrastructure.
* **Division-by-Zero Protection:** Incorporates mathematical boundaries to ensure the application won't crash when your mouth is closed completely.
* **Dynamic Camera Binding:** Scans your physical machine endpoints automatically to find and lock onto the correct video stream sequence.

---

##  System Requirements & Libraries

This application requires **Python 3.10+** along with the following primary distribution libraries:

* `opencv-python` (Webcam image capture framework and layout drawing tools)
* `cvzone` (Facial Mesh pipeline engine used to retrieve precise keypoints)
* `numpy` (Vector math structures to track spatial coordinate distance differences)

---

##  Installation & Operation Steps

Run these setup blocks directly inside your active terminal environment:

### 1. Synchronize Project Dependencies
Ensure your project virtual environment (`.venv`) is active, then run this unified setup command:
```powershell
pip install opencv-python cvzone numpy
```

### 2. Launch the Application Script
Navigate directly to this sub-workspace folder structure and run the execution script:
```powershell
cd "OpenCV/Yawn Detector"
python yawn_detector.py
```

---

##  How the Detection Math Works

The script monitors **4 distinct geometric coordinate regions** on your mouth:
* **Landmark 13 & 14:** The top and bottom thresholds of the inner lips (Vertical Depth).
* **Landmark 78 & 308:** The left and right perimeter boundary points of the mouth corners (Horizontal Breadth).

### The Geometric Ratio Equation:
$$\text{Mouth Ratio} = \frac{\text{Horizontal Distance between Corners}}{\text{Vertical Distance between Lips}}$$

* **Mouth Closed / Normal Speech:** The vertical distance is tiny, generating a **high numerical ratio** (typically $> 2.5$).
* **Yawning:** The vertical distance expands exponentially, causing the overall **ratio value to drop heavily** below the critical threshold limit ($\le 1.8$), which instantly prints the tracking alarm on your display screen.

---

## Trouble Resolutions

* **Webcam Window Remains Black / Fails to Boot:**
  Close other software layers actively claiming exclusive camera streams (e.g., Zoom, Microsoft Teams, OBS Studio, Discord, or open browser video chats).
* **Tracking Warning Appears Too Early / Too Late:**
  If your typical talking style triggers false alarms, open `yawn_detector.py` and adjust the numerical trigger index limit slightly on **line 58** (`if ratio < 1.8:`) down to `1.6` for lower sensitivity, or up to `2.0` for higher sensitivity.
