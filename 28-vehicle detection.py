import cv2

cap = cv2.VideoCapture(r"F:\vehicle_traffic.mp4")

if not cap.isOpened():
    print("Error: Cannot open video")
    exit()

# Better background subtractor settings for crowded scenes
bg_subtractor = cv2.createBackgroundSubtractorMOG2(
    history=300,          # shorter history = adapts faster
    varThreshold=25,      # lower threshold = more detections
    detectShadows=False
)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    fg_mask = bg_subtractor.apply(frame, learningRate=0.01)

    # Reduce noise but keep vehicle shapes
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, kernel)
    fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_DILATE, kernel)

    # Find contours (moving objects)
    contours, _ = cv2.findContours(
        fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    for cnt in contours:
        area = cv2.contourArea(cnt)

        # Much smaller threshold → detects more vehicles
        if area > 200:   # earlier you used 800
            x, y, w, h = cv2.boundingRect(cnt)

            # Optional: ignore very tall/wide blobs (buildings, shadows)
            if w > 20 and h > 20:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, "Vehicle", (x, y-5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.45,
                            (0, 255, 0), 1)

    cv2.imshow("Vehicle Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
