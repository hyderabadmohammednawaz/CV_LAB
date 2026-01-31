import cv2, os

print(os.getcwd())
v = cv2.VideoCapture(r"E:\sample_video.mp4")

if not v.isOpened():
    print("Video not found")
    exit()

fps = v.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps)  # normal speed

cv2.namedWindow("Video", cv2.WINDOW_NORMAL)

while True:
    r, f = v.read()
    if not r:
        break

    cv2.imshow("Video", f)

    k = cv2.waitKey(delay) & 0xFF

    if k == ord('n'):      # Normal
        delay = int(1000 / fps)
        print("Normal speed")

    elif k == ord('s'):    # Slow
        delay = int(1000 / (fps / 3))
        print("Slow motion")

    elif k == ord('f'):    # Fast
        delay = int(1000 / (fps * 2))
        print("Fast motion")

    elif k == ord('q'):    # Quit
        print("Exiting...")
        break

v.release()
cv2.destroyAllWindows()
