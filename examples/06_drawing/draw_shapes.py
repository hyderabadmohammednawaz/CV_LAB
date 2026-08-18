"""Draw shapes on images (rectangles, circles, text).

Useful for:
- Annotating images
- Highlighting regions of interest
- Creating overlays
- Visualization
"""

import cv2
import numpy as np


def draw_shapes(image_path):
    """Draw various shapes on an image.
    
    Args:
        image_path (str): Path to the input image
    
    Returns:
        np.ndarray: Image with drawn shapes
    """
    image = cv2.imread(image_path)
    
    if image is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    
    result = image.copy()
    h, w = image.shape[:2]
    
    # Draw rectangle
    cv2.rectangle(result, (50, 50), (200, 150), (0, 255, 0), 2)
    
    # Draw filled circle
    cv2.circle(result, (w//2, h//2), 50, (0, 0, 255), -1)
    
    # Draw line
    cv2.line(result, (0, 0), (w, h), (255, 0, 0), 2)
    
    # Draw text
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(result, 'CV_LAB', (50, 300), font, 1, (255, 255, 255), 2)
    
    return image, result


def main():
    """Main execution function."""
    image_path = r"E:\image.jpg"  # Change this path
    
    try:
        image, result = draw_shapes(image_path)
        
        cv2.imshow("Original", image)
        cv2.imshow("With Shapes", result)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except FileNotFoundError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
