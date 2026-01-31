import cv2

image = cv2.imread(r"F:\car.jpg")  # BHANUTEJA REDDY

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    watch_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    objects = watch_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in objects:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Detected Object", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not loaded! Check the path.")
