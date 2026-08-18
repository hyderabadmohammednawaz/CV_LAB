"""Detect faces in an image using Haar Cascade Classifier.

Haar Cascades are trained classifiers that detect features
by looking for patterns of intensity changes.

Useful for:
- Face detection in images
- Real-time face detection in video
- Preprocessing for facial recognition
"""

import cv2
import numpy as np


def detect_faces(image_path):
    """Detect faces in an image.
    
    Args:
        image_path (str): Path to the input image
    
    Returns:
        tuple: Original image and image with detected faces marked
    """
    # Load face cascade classifier
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )
    
    # Read image
    image = cv2.imread(image_path)
    
    if image is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    
    # Draw rectangles around faces
    image_with_faces = image.copy()
    for (x, y, w, h) in faces:
        cv2.rectangle(image_with_faces, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    return image, image_with_faces, len(faces)


def main():
    """Main execution function."""
    image_path = r"F:\ratan sir.jpg"  # Change this path
    
    try:
        image, result, count = detect_faces(image_path)
        
        print(f"Detected {count} face(s)")
        
        cv2.imshow("Original", image)
        cv2.imshow("Face Detection", result)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except FileNotFoundError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
