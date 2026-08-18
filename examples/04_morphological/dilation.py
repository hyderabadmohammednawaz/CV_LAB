"""Apply morphological dilation.

Dilation expands white regions (foreground) in the image.
Useful for:
- Filling small holes
- Connecting nearby objects
- Thickening features
"""

import cv2
import numpy as np


def apply_dilation(image_path, kernel_size=5, iterations=1):
    """Apply morphological dilation.
    
    Args:
        image_path (str): Path to the input image
        kernel_size (int): Size of the dilation kernel
        iterations (int): Number of dilation iterations
    
    Returns:
        tuple: Original and dilated image
    """
    image = cv2.imread(image_path)
    
    if image is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    
    # Create kernel
    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT,
        (kernel_size, kernel_size)
    )
    
    # Apply dilation
    dilated = cv2.dilate(image, kernel, iterations=iterations)
    
    return image, dilated


def main():
    """Main execution function."""
    image_path = r"E:\image.jpg"  # Change this path
    
    try:
        image, dilated = apply_dilation(image_path, kernel_size=5, iterations=1)
        
        cv2.imshow("Original", image)
        cv2.imshow("Dilated", dilated)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except FileNotFoundError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
