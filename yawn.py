#Author: Shashank Hegde
#Institute: Moodlakatte Institute of Technology, Kundapura
import cv2
import numpy as np
from cvzone.FaceMeshModule import FaceMeshDetector

# 1. Automated Camera Index Finder
cap = None
for index in [0, 1, 2, -1]:
    cap = cv2.VideoCapture(index)
    if cap.isOpened():
        print(f"--> Webcam successfully connected on Index [{index}]!")
        break
    cap.release()

if not cap or not cap.isOpened():
    print("CRITICAL ERROR: No working webcam found. Please close other camera apps.")
    exit()

# 2. Initialize the Face Mesh Detector (looks for 1 face)
detector = FaceMeshDetector(maxFaces=1)

print("Setup complete. Opening Yawn Detector... (Press 'q' to quit)")

while True:
    success, img = cap.read()
    if not success:
        continue

    # Find face mesh landmarks automatically
    img, faces = detector.findFaceMesh(img, draw=False)

    if faces:
        face = faces[0]

        # Landmark indices for the inner lips:
        # 13: Top Lip Center | 14: Bottom Lip Center
        # 78: Left Corner   | 308: Right Corner
        top_lip = face[13]
        bottom_lip = face[14]
        left_corner = face[78]
        right_corner = face[308]

        # Calculate absolute pixel distances using OpenCV's norm tool
        ver_dist = cv2.norm(np.array(top_lip) - np.array(bottom_lip))
        hor_dist = cv2.norm(np.array(left_corner) - np.array(right_corner))

        # Safe-guard calculation: Avoid division by zero if lips match exactly
        if ver_dist == 0:
            ratio = 99.0
        else:
            ratio = hor_dist / ver_dist

        # Draw the target dots on the mouth for visual feedback
        for pt in [top_lip, bottom_lip, left_corner, right_corner]:
            cv2.circle(img, (pt[0], pt[1]), 3, (0, 255, 0), cv2.FILLED)

        # When yawning, the vertical distance increases, so the horizontal/vertical ratio drops
        if ratio < 1.8:
            cv2.putText(img, "YAWNING!", (50, 100), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 4)

    # Show live tracking window
    cv2.imshow("Yawn Detector Workspace", img)

    # Press 'q' on your keyboard to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Application closed down safely.")
