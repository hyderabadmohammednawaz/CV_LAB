<!-- Image assets directory for README and documentation -->

<!-- To add images, place them in this directory and reference them in markdown as: -->
<!-- ![Alt text](assets/image-name.png) -->

<!-- Required images for professional README: -->
<!-- 1. cv_banner.png - Main banner (1200x400) -->
<!-- 2. workflow.png - CV workflow diagram (800x600) -->
<!-- 3. image-manipulation.png - Image manipulation examples (800x400) -->
<!-- 4. transformations.png - Geometric transformations (800x400) -->
<!-- 5. features.png - Feature detection examples (800x400) -->
<!-- 6. morphological.png - Morphological operations (800x400) -->
<!-- 7. detection.png - Object detection examples (800x400) -->
<!-- 8. logo.png - Repository logo (200x200) -->

# Assets Directory

This directory contains all images and media used in documentation.

## Image Naming Convention

- Use descriptive lowercase names with hyphens
- Use PNG format for graphics and screenshots
- Use JPG for photographs
- Keep file sizes optimized (<500KB each)

## Creating Missing Images

To generate the required banner images, you can:

1. **Use Python with PIL/Pillow**:
```python
from PIL import Image, ImageDraw, ImageFont

# Create CV_LAB banner
img = Image.new('RGB', (1200, 400), color='#1e3a8a')
draw = ImageDraw.Draw(img)
draw.text((300, 150), 'CV_LAB', fill='white', font=None)
img.save('cv_banner.png')
```

2. **Use Online Tools**:
- Canva.com
- Figma.com
- GIMP (free desktop tool)

3. **Use Screenshots**:
Capture relevant sections from running examples and resize appropriately.

## Image Specifications

| Image | Dimensions | Format | Purpose |
|-------|------------|--------|----------|
| cv_banner.png | 1200x400 | PNG | Main header banner |
| workflow.png | 800x600 | PNG | CV workflow diagram |
| image-manipulation.png | 800x400 | PNG | Manipulation examples |
| transformations.png | 800x400 | PNG | Transformation examples |
| features.png | 800x400 | PNG | Feature detection |
| morphological.png | 800x400 | PNG | Morphological operations |
| detection.png | 800x400 | PNG | Detection examples |
| logo.png | 200x200 | PNG | Repository logo |

## Adding Images to README

```markdown
<div align="center">
  <img src="assets/image-name.png" alt="Description" width="80%" />
</div>
```
