"""Rotate image 90 degrees on Y-axis."""

import cv2
import numpy as np


def rotate_90_y_axis(image_path):
    """Rotate image 90 degrees around Y-axis.
    
    Args:
        image_path (str): Path to the input image
    
    Returns:
        tuple: Original and rotated image
    """
    image = cv2.imread(image_path)
    
    if image is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    
    # Rotate 90 degrees
    rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    
    return image, rotated


def main():
    """Main execution function."""
    image_path = r"E:\image.jpg"  # Change this path
    
    try:
        image, rotated = rotate_90_y_axis(image_path)
        
        cv2.imshow("Original", image)
        cv2.imshow("Rotated 90°", rotated)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except FileNotFoundError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
