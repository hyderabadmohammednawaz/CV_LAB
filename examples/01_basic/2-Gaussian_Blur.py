"""Apply Gaussian blur to an image.

Gaussian blur is used to:
- Reduce image noise
- Smooth out details
- Prepare images for further processing
- Create artistic effects

The kernel size determines the blur intensity.
"""

import cv2
import numpy as np


def apply_gaussian_blur(image_path, kernel_size=(15, 15)):
    """Apply Gaussian blur to an image.
    
    Args:
        image_path (str): Path to the input image
        kernel_size (tuple): Blur kernel size (must be odd)
    
    Returns:
        tuple: Original and blurred image
    """
    image = cv2.imread(image_path)
    
    if image is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    
    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(image, kernel_size, 0)
    
    return image, blurred_image


def main():
    """Main execution function."""
    image_path = r"E:\eagle.jpg"  # Change this path
    
    try:
        image, blurred = apply_gaussian_blur(image_path, kernel_size=(15, 15))
        
        cv2.imshow("Original Image", image)
        cv2.imshow("Blurred Image", blurred)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except FileNotFoundError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
