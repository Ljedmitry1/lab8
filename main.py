import time
import cv2
import numpy as np

def image_processing():
    while True:
        img = cv2.imread("lab8/test.png")
        blur = cv2.GaussianBlur(img, (31,31), 0)
        hor_c = np.hstack((img, blur))
        cv2.imshow('img+blur', hor_c)

        if cv2.waitKey(1) == ord('q'):
            break
    

if __name__ == "__main__":
    image_processing()

cv2.destroyAllWindows()
