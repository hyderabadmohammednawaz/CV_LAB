# CV_LAB - Computer Vision Learning Laboratory

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.5+-green.svg)](https://opencv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/hyderabadmohammednawaz/CV_LAB)
[![GitHub Stars](https://img.shields.io/github/stars/hyderabadmohammednawaz/CV_LAB?style=social)](https://github.com/hyderabadmohammednawaz/CV_LAB)

<div align="center">
  <img src="assets/cv_banner.png" alt="CV_LAB Banner" width="100%" />
</div>

## 📋 Overview

CV_LAB is a comprehensive Computer Vision learning repository containing **40+ practical examples** covering fundamental to advanced image processing techniques using OpenCV and Python. Perfect for students, researchers, and developers learning computer vision concepts.

<div align="center">
  <img src="assets/workflow.png" alt="Computer Vision Workflow" width="80%" />
</div>

## 🎯 Key Features

- **40+ Hands-on Examples**: From grayscale conversion to advanced detection algorithms
- **Well-Organized Structure**: Categorized by concept and complexity
- **Real-World Applications**: Face detection, vehicle detection, object recognition, and more
- **Educational Focus**: Each example is self-contained and well-commented
- **Easy to Use**: Simple setup, minimal dependencies
- **CI/CD Ready**: GitHub Actions workflows for automated testing
- **Professional Documentation**: Comprehensive guides and API references

## 📚 Topics Covered

### Image Manipulation (1-9)
<div align="center">
  <img src="assets/image-manipulation.png" alt="Image Manipulation Examples" width="70%" />
</div>

- Grayscale conversion
- Gaussian blur
- Edge detection (Canny)
- Histogram equalization
- Image erosion/dilation
- Video processing

### Geometric Transformations (10-14)
<div align="center">
  <img src="assets/transformations.png" alt="Geometric Transformations" width="70%" />
</div>

- 90° rotation (Y-axis)
- 180° rotation (Y-axis)
- 270° rotation (Y-axis)
- Affine transformations
- Perspective transformations

### Feature Detection (15-16)
<div align="center">
  <img src="assets/features.png" alt="Feature Detection" width="70%" />
</div>

- Harris corner detection
- Sobel edge detection

### Advanced Techniques (17-24)
<div align="center">
  <img src="assets/morphological.png" alt="Morphological Operations" width="70%" />
</div>

- Watermarking
- Region of Interest (ROI)
- Morphological operations (Erosion, Dilation)
- Opening/Closing techniques
- Top hat/Black hat transforms

### Object & Face Detection (25-40)
<div align="center">
  <img src="assets/detection.png" alt="Object Detection Examples" width="70%" />
</div>

- Object recognition
- Face detection
- Vehicle detection
- Eye detection
- Smile detection
- Image segmentation
- Drawing primitives (rectangles, circles, text)
- Background/foreground removal
- Face counting
- Video manipulation
- Text extraction from video

## 🚀 Quick Start

### Prerequisites

```bash
Python 3.8 or higher
Pip package manager
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/hyderabadmohammednawaz/CV_LAB.git
cd CV_LAB
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

### Running Examples

```bash
# Run any example
python examples/01_basic/1-gray_scale.py

# Run with Makefile
make run-example FILE=examples/01_basic/1-gray_scale.py
```

## 📁 Project Structure

```
CV_LAB/
├── examples/
│   ├── 01_basic/              # Image manipulation basics
│   ├── 02_transformations/    # Geometric transformations
│   ├── 03_features/           # Feature detection
│   ├── 04_morphological/      # Morphological operations
│   ├── 05_detection/          # Object & face detection
│   └── 06_drawing/            # Drawing & annotation
├── docs/
│   ├── CONTRIBUTING.md        # Contribution guidelines
│   ├── SETUP.md              # Detailed setup guide
│   └── TOPICS.md             # Topic explanations
├── tests/
│   ├── test_examples.py      # Basic test suite
│   └── conftest.py           # Pytest configuration
├── assets/                    # Images for README and examples
├── requirements.txt           # Python dependencies
├── Makefile                   # Development commands
├── .github/workflows/         # CI/CD pipelines
├── LICENSE                    # MIT License
└── README.md                  # This file
```

## 💻 System Requirements

- **OS**: Windows, macOS, or Linux
- **RAM**: 2GB minimum (4GB recommended)
- **Disk Space**: 500MB for repository + sample images
- **Python**: 3.8+

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|----------|
| opencv-python | 4.5+ | Core computer vision library |
| numpy | 1.20+ | Numerical computations |
| matplotlib | 3.3+ | Visualization |
| pillow | 8.0+ | Image processing |

## 📊 Learning Path

```
Beginner
  ↓
Examples 1-9 (Basic image manipulation)
  ↓
Intermediate
  ↓
Examples 10-24 (Transformations & features)
  ↓
Advanced
  ↓
Examples 25-40 (Detection & recognition)
```

**Beginner**: Examples 1-9 (Basic image manipulation)  
**Intermediate**: Examples 10-24 (Transformations & features)  
**Advanced**: Examples 25-40 (Detection & recognition)  

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

### Ways to Contribute
- Report bugs and issues
- Add new computer vision examples
- Improve documentation
- Optimize code performance
- Add comprehensive test coverage
- Share your projects built with CV_LAB

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## 🔗 Resources

- [OpenCV Documentation](https://docs.opencv.org/)
- [OpenCV Tutorials](https://docs.opencv.org/master/d9/df8/tutorial_root.html)
- [NumPy Documentation](https://numpy.org/doc/)
- [Matplotlib Documentation](https://matplotlib.org/)
- [Computer Vision Papers](https://paperswithcode.com/area/computer-vision)

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/hyderabadmohammednawaz/CV_LAB/issues)
- **Discussions**: [GitHub Discussions](https://github.com/hyderabadmohammednawaz/CV_LAB/discussions)
- **Email**: hyderabadmohammednawaz@gmail.com

## 🌟 Show Your Support

If this repository helped you learn computer vision, please consider:
- ⭐ Starring the repository
- 👥 Following the author
- 📤 Sharing with others
- 🤝 Contributing improvements
- 💬 Providing feedback

## 📈 Repository Stats

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/hyderabadmohammednawaz/CV_LAB)
![GitHub last commit](https://img.shields.io/github/last-commit/hyderabadmohammednawaz/CV_LAB)
![GitHub repo size](https://img.shields.io/github/repo-size/hyderabadmohammednawaz/CV_LAB)

## 🏆 Showcase Projects

Built something with CV_LAB? Let us know! We'd love to feature your project.

---

<div align="center">
  <strong>Happy Learning! 🎉</strong>
  
  Made with ❤️ by Mohammed Nawaz  
  Last Updated: January 2026  
  Status: Active Maintenance ✓
</div>
