import numpy as np
import cv2
import matplotlib.pyplot as plt

def create_rectangle_image(image_size):

    height, width = image_size

    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    top_left = (width // 4, height // 4)
    bottom_right = (3 * width // 4, 3 * height // 4)

    cv2.rectangle(image, top_left, bottom_right, (255, 0, 0), 2)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.imshow(image_rgb)
    plt.axis("off")
    plt.title("Rectangle Image")
    plt.show()

user_width = int(input("Enter image width: "))
user_height = int(input("Enter image height: "))#BHANUTEJA REDDY

create_rectangle_image((user_height, user_width))
