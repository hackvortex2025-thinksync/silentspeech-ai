import cv2

def get_lip_frames():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Webcam not accessible.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Webcam Feed", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()