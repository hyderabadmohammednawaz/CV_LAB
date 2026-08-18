#!/usr/bin/env python3
"""
Script to create sample images for documentation.
Run this to generate placeholder images.
"""

import numpy as np
import cv2
import os
from pathlib import Path


def create_sample_image(filename, width=400, height=300):
    """Create a sample image with gradient and text."""
    img = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Create gradient
    for i in range(width):
        img[:, i] = [i % 256, (i * 2) % 256, (i * 3) % 256]
    
    # Add text
    cv2.putText(img, 'CV_LAB', (50, 150), 
                cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)
    
    cv2.imwrite(filename, img)
    print(f"Created: {filename}")


def create_banner():
    """Create CV_LAB banner."""
    img = np.zeros((400, 1200, 3), dtype=np.uint8)
    
    # Blue gradient background
    for i in range(1200):
        img[:, i] = [30 + int(60 * i / 1200), 58, 138]
    
    # Add text
    cv2.putText(img, 'CV_LAB: Computer Vision Learning Lab', (150, 200),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)
    cv2.putText(img, '40+ Practical Examples | OpenCV | Python', (250, 280),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (200, 200, 200), 1)
    
    cv2.imwrite('assets/cv_banner.png', img)
    print("Created: assets/cv_banner.png")


def create_workflow_diagram():
    """Create workflow diagram."""
    img = np.ones((600, 800, 3), dtype=np.uint8) * 255
    
    # Draw boxes and text for workflow
    cv2.rectangle(img, (50, 100), (200, 180), (52, 152, 219), 2)
    cv2.putText(img, 'Image Input', (60, 145), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 1)
    
    cv2.arrowedLine(img, (200, 140), (300, 140), (0, 0, 0), 2)
    
    cv2.rectangle(img, (300, 100), (450, 180), (46, 204, 113), 2)
    cv2.putText(img, 'Processing', (310, 145), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 1)
    
    cv2.arrowedLine(img, (450, 140), (550, 140), (0, 0, 0), 2)
    
    cv2.rectangle(img, (550, 100), (700, 180), (231, 76, 60), 2)
    cv2.putText(img, 'Output', (590, 145), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 1)
    
    # Add more details
    cv2.putText(img, 'Basic Manipulation | Transformations', (50, 300),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 1)
    cv2.putText(img, 'Feature Detection | Morphological Ops', (50, 350),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 1)
    cv2.putText(img, 'Object Detection | Video Processing', (50, 400),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 1)
    
    cv2.imwrite('assets/workflow.png', img)
    print("Created: assets/workflow.png")


def main():
    """Create all sample images."""
    # Create assets directory
    Path('assets').mkdir(exist_ok=True)
    
    print("Generating sample images...")
    print()
    
    create_banner()
    create_workflow_diagram()
    
    # Create other sample images
    sample_images = [
        ('assets/image-manipulation.png', 'Image Manipulation'),
        ('assets/transformations.png', 'Transformations'),
        ('assets/features.png', 'Feature Detection'),
        ('assets/morphological.png', 'Morphological Ops'),
        ('assets/detection.png', 'Object Detection'),
    ]
    
    for filepath, label in sample_images:
        create_sample_image(filepath)
    
    print()
    print("✓ All sample images created successfully!")
    print("  Located in: assets/")


if __name__ == '__main__':
    main()
