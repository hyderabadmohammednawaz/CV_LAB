"""Apply morphological erosion.

Erosion shrinks white regions (foreground) in the image.
Useful for:
- Removing small objects
- Separating connected objects
- Thinning features
"""

import cv2
import numpy as np


def apply_erosion(image_path, kernel_size=5, iterations=1):
    """Apply morphological erosion.
    
    Args:
        image_path (str): Path to the input image
        kernel_size (int): Size of the erosion kernel
        iterations (int): Number of erosion iterations
    
    Returns:
        tuple: Original and eroded image
    """
    image = cv2.imread(image_path)
    
    if image is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    
    # Create kernel
    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT, 
        (kernel_size, kernel_size)
    )
    
    # Apply erosion
    eroded = cv2.erode(image, kernel, iterations=iterations)
    
    return image, eroded


def main():
    """Main execution function."""
    image_path = r"E:\image.jpg"  # Change this path
    
    try:
        image, eroded = apply_erosion(image_path, kernel_size=5, iterations=1)
        
        cv2.imshow("Original", image)
        cv2.imshow("Eroded", eroded)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except FileNotFoundError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
