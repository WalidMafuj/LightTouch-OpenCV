import cv2
import numpy as np
import time as tm
import urllib.request
import mouse

url = "http://192.168.0.3:8080/shot.jpg"
cap = cv2.VideoCapture(0)
xo=1920
x=2943
y=767

file1  = open("x.txt", "r")
pointx = file1.read()
pointx = pointx.split(' ')
print(pointx)
file2  = open("y.txt", "r")
pointy = file2.read()
pointy = pointy.split(' ')
print(pointy)

while (1):
    imgresp = urllib.request.urlopen(url)
    imgnp = np.array(bytearray(imgresp.read()), dtype=np.uint8)
    frame = cv2.imdecode(imgnp, -1)


    pts1 = np.float32([[pointx[0], pointy[0]], [pointx[1], pointy[1]], [pointx[2], pointy[2]], [pointx[3], pointy[3]]])
    pts2 = np.float32([[xo, 0], [xo, y], [x, 0], [x, y]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(frame, matrix, (x, y))

    plot = np.zeros((frame.shape[0], frame.shape[1], 3), dtype="uint8")
    blr = cv2.GaussianBlur(result, (15, 15), 0)
    gray = cv2.cvtColor(blr, cv2.COLOR_BGR2GRAY)
    (t, binImg) = cv2.threshold(gray, 150, 170, cv2.THRESH_BINARY_INV)
    cnts, hrchy = cv2.findContours(binImg, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    n = len(cnts) - 1
    cnts = sorted(cnts, key=cv2.contourArea, reverse=False)[:n]
    if len(cnts) > 0:
        print(len(cnts))
    for c in cnts:
        hull = cv2.convexHull(c)

    try:
        M = cv2.moments(cnts[0])
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        print(cx,cy)
        mouse.move(cx,cy)
        mouse.click()
        cv2.circle(result,(cx,cy),3,(0,0,255),2)
    except:
        pass
    cv2.imshow('res', result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        exit(0)
    if cv2.waitKey(1) & 0xFF == ord('m'):
        exit(0)
    # print(r,g,b,noOfcountors)
cv2.destroyAllWindows()
cap.release()
