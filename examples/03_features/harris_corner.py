"""Detect corners using Harris corner detection.

Harris corner detection identifies points where:
- Intensity changes rapidly in multiple directions
- Corners and edges are highlighted

Useful for:
- Feature matching
- Image alignment
- 3D reconstruction
"""

import cv2
import numpy as np


def detect_corners_harris(image_path):
    """Detect corners using Harris corner detection.
    
    Args:
        image_path (str): Path to the input image
    
    Returns:
        tuple: Original image and corner response map
    """
    image = cv2.imread(image_path)
    
    if image is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    
    # Detect corners
    corners = cv2.cornerHarris(gray, 2, 3, 0.04)
    
    # Normalize and scale for visualization
    corners = cv2.normalize(corners, None)
    corners_scaled = (corners * 255).astype(np.uint8)
    
    # Draw corners on image
    image_with_corners = image.copy()
    image_with_corners[corners > 0.01 * corners.max()] = [0, 0, 255]
    
    return image, image_with_corners


def main():
    """Main execution function."""
    image_path = r"E:\image.jpg"  # Change this path
    
    try:
        image, corners = detect_corners_harris(image_path)
        
        cv2.imshow("Original", image)
        cv2.imshow("Harris Corners", corners)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except FileNotFoundError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
