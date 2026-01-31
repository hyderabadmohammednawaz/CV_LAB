import cv2
import os

def play_video_reverse_slow(video_path):
    if not os.path.exists(video_path):
        print("File not found:", video_path)
        return

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Video could not be opened")
        return

    frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()

    print("Frames loaded:", len(frames))

    for frame in frames[::-1]:
        cv2.imshow("Reverse Slow Motion Video", frame)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
play_video_reverse_slow(r"E:\sample_video.mp4")#BHANUTEJA REDDY
