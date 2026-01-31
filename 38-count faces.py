import cv2
import matplotlib.pyplot as plt

def count_faces(image_path):

    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found!")
        return 0
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Improve contrast for better detection
    gray = cv2.GaussianBlur(gray, (5,5), 0)
    gray = cv2.equalizeHist(gray)
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.03,      # detect smaller / closer faces
        minNeighbors=5,       # allow close / overlapping faces
        minSize=(40, 40),     # don't miss smaller faces
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    print("Number of faces detected:", len(faces))
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0,255,0), 2)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(8,6))
    plt.imshow(image)
    plt.axis("off")
    plt.show()
    return len(faces)
count_faces(r"E:\group.jpg")#BHANUTEJA REDDY
