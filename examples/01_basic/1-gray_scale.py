"""Convert image to grayscale.

Grayscale conversion transforms a color image into shades of gray.
This is useful for:
- Reducing data size
- Simplifying processing
- Preparing for edge detection
- Improving performance
"""

import cv2
import numpy as np


def convert_to_grayscale(image_path):
    """Convert an image to grayscale.
    
    Args:
        image_path (str): Path to the input image
    
    Returns:
        tuple: Original image and grayscale image
    """
    # Read the image
    image = cv2.imread(image_path)
    
    if image is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    
    # Convert BGR to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    return image, gray_image


def main():
    """Main execution function."""
    # Example: Replace with your image path
    image_path = r"E:\image.jpg"  # Change this path
    
    try:
        image, gray_image = convert_to_grayscale(image_path)
        
        # Display results
        cv2.imshow("Original Image", image)
        cv2.imshow("Grayscale Image", gray_image)
        
        print("Original shape:", image.shape)
        print("Grayscale shape:", gray_image.shape)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except FileNotFoundError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
