"""Detect edges using Canny edge detection.

Canny edge detection is a multi-stage algorithm that:
1. Reduces noise with Gaussian blur
2. Calculates image gradients
3. Applies non-maximum suppression
4. Uses double thresholding and edge tracking

Useful for:
- Boundary detection
- Object outline detection
- Image segmentation
"""

import cv2
import numpy as np


def detect_edges_canny(image_path, threshold1=100, threshold2=200):
    """Detect edges using Canny algorithm.
    
    Args:
        image_path (str): Path to the input image
        threshold1 (int): Lower threshold
        threshold2 (int): Upper threshold
    
    Returns:
        tuple: Original and edge-detected image
    """
    image = cv2.imread(image_path)
    
    if image is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Canny edge detection
    edges = cv2.Canny(gray, threshold1, threshold2)
    
    return image, edges


def main():
    """Main execution function."""
    image_path = r"E:\image.jpg"  # Change this path
    
    try:
        image, edges = detect_edges_canny(image_path)
        
        cv2.imshow("Original Image", image)
        cv2.imshow("Edges (Canny)", edges)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except FileNotFoundError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
