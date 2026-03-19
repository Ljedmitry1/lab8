import cv2
import numpy as np


def video_mark():
    cap = cv2.VideoCapture(0)
    file = open('coords.txt', 'w')
    file.write('\tX\tY\n')
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        red_mask = cv2.inRange(frame, (0, 0, 100), (50, 50, 255))
        
        points = np.where(red_mask > 0)
        
        if len(points[0]) > 0:
            y, x = points[0][0], points[1][0]
            file.write(f"\t{x}\t{y}\n")
            file.flush()
            cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
        
        cv2.imshow('mark', frame)
        
        if cv2.waitKey(1) == ord('q'):
            break
    file.close()
    cap.release()

if __name__ == '__main__':
    video_mark()

cv2.destroyAllWindows()
