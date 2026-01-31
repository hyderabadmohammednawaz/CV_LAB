import cv2
import os

def extract_text_from_video(video_path, frame_skip=30, output_folder="extracted_frames"):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Cannot open video")
        return

    os.makedirs(output_folder, exist_ok=True)

    frame_count = 0
    saved = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1

        display_frame = frame.copy()

        # If this frame is being extracted, mark it visually
        if frame_count % frame_skip == 0:
            filename = os.path.join(output_folder, f"frame_{saved}.jpg")
            cv2.imwrite(filename, frame)
            saved += 1

            # Draw RED border to show extraction
            cv2.rectangle(display_frame,
                          (10, 10), (frame.shape[1]-10, frame.shape[0]-10),
                          (0, 0, 255), 5)

            cv2.putText(display_frame, "EXTRACTED FRAME",
                        (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 0, 255), 2)

        cv2.imshow("Video - Extracting Frames", display_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"Extracted {saved} key frames for text analysis.")
extract_text_from_video(r"E:\sample_video.mp4")

