import cv2

image = cv2.imread(r"F:\eagle.jpg")#BHANUTEJA REDDY

if image is not None:
    H, W, _ = image.shape

    x, y, w, h = 100, 50, 175, 133

    x2 = min(x + w, W)
    y2 = min(y + h, H)

    roi = image[y:y2, x:x2]

    h_roi, w_roi, _ = roi.shape

    paste_x = W - w_roi - 10
    paste_y = H - h_roi - 10

    image[paste_y:paste_y+h_roi, paste_x:paste_x+w_roi] = roi

    cv2.imshow("Image", image)
    cv2.imshow("ROI", roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
