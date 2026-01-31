import cv2

original = cv2.imread(r"F:\nature.jpg")
watermark = cv2.imread(r"F:\logo.png")

if original is None:
    print("Original image not found")
elif watermark is None:
    print("Watermark image not found")
else:
    watermark = cv2.resize(watermark, (original.shape[1], original.shape[0]))

    alpha = 0.3
    watermarked = cv2.addWeighted(original, 1 - alpha, watermark, alpha, 0)

    cv2.imwrite("watermarked_output.jpg", watermarked)

    cv2.imshow("Original", original)
    cv2.imshow("Watermark", watermark)
    cv2.imshow("Watermarked Image", watermarked)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
