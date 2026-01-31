import numpy as np
import matplotlib.pyplot as plt

def create_colored_corners(image_size):

    height, width = image_size

    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    box_h, box_w = height // 10, width // 10

    image[:box_h, :box_w] = [0, 0, 0]
    image[:box_h, -box_w:] = [255, 0, 0]
    image[-box_h:, :box_w] = [0, 255, 0]
    image[-box_h:, -box_w:] = [0, 0, 255]

    plt.imshow(image)
    plt.axis("off")
    plt.title("Colored Corners Image")
    plt.show()

user_width = int(input("Enter image width: "))
user_height = int(input("Enter image height: "))#BHANUTEJA REDDY

create_colored_corners((user_height, user_width))
