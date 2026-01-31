import numpy as np
import cv2
import matplotlib.pyplot as plt

def create_circle_image(image_size):

    height, width = image_size

    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    center = (width // 2, height // 2)
    radius = min(width, height) // 4

    cv2.circle(image, center, radius, (0, 0, 255), 2)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.imshow(image_rgb)
    plt.axis("off")
    plt.title("Circle Image")
    plt.show()

user_width = int(input("Enter image width: "))
user_height = int(input("Enter image height: "))#BHANUTEJA REDDY

create_circle_image((user_height, user_width))
