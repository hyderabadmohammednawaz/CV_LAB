import cv2

def detect_smile(image_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found!")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(60, 60))

    for (x, y, w, h) in faces:

        mouth_y = y + int(h * 0.6)
        mouth_h = int(h * 0.4)

        mouth_roi = gray[mouth_y:mouth_y + mouth_h, x:x + w]

        smiles = smile_cascade.detectMultiScale(mouth_roi, 1.3, 10, minSize=(20, 20))

        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(image, (x + sx, mouth_y + sy), (x + sx + sw, mouth_y + sy + sh), (0, 255, 0), 2)

    cv2.imshow("Smile Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

detect_smile(r"F:\smiling.jpg")
