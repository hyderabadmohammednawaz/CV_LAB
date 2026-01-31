import cv2
import os

def reverse_video(input_path, output_path="reversed_video.mp4"):

    if not os.path.exists(input_path):
        print("Error: Video file not found!")
        return

    cap = cv2.VideoCapture(input_path)

    if not cap.isOpened():
        print("Error: Cannot open video (codec issue).")
        return

    frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()

    print("Total frames read:", len(frames))

    if len(frames) == 0:
        print("Error: No frames read from video.")
        return

    height, width, _ = frames[0].shape

    # Get original FPS
    cap = cv2.VideoCapture(input_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    cap.release()

    out = cv2.VideoWriter(
        output_path,
        cv2.VideoWriter_fourcc(*'mp4v'),
        fps,
        (width, height)
    )

    # Write frames in reverse order
    for frame in frames[::-1]:
        out.write(frame)

    out.release()
    print("Reversed video saved as:", output_path)


# --------- MAIN CALL ---------
reverse_video(r"F:\sample_video.mp4")
