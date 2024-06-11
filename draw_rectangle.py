import cv2

image = cv2.imread("Image_Video/image.png")
while True:
    cv2.rectangle(image, (49, 145), (156, 193), (255, 100, 100), 2)
    cv2.imshow("Input Image", image)
    if cv2.waitKey(10) & 0xFF==ord('1'):
        break