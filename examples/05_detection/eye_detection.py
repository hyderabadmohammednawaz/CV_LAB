"""Detect eyes in faces using Haar Cascade Classifier.

Eye detection requires:
1. First detecting faces
2. Then detecting eyes within face regions

Useful for:
- Gaze detection
- Face recognition preprocessing
- Attention detection
"""

import cv2
import numpy as np


def detect_eyes(image_path):
    """Detect eyes in an image.
    
    Args:
        image_path (str): Path to the input image
    
    Returns:
        tuple: Original image and image with detected eyes marked
    """
    # Load cascades
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )
    eye_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_eye.xml'
    )
    
    # Read image
    image = cv2.imread(image_path)
    
    if image is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    image_with_eyes = image.copy()
    
    # For each face, detect eyes
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image_with_eyes[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 255), 2)
    
    return image, image_with_eyes


def main():
    """Main execution function."""
    image_path = r"F:\face_image.jpg"  # Change this path
    
    try:
        image, result = detect_eyes(image_path)
        
        cv2.imshow("Original", image)
        cv2.imshow("Eye Detection", result)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except FileNotFoundError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
