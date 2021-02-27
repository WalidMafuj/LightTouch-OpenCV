import cv2
import numpy as np
import time as tm
import urllib.request
url = "http://192.168.0.3:8080/shot.jpg"
cap = cv2.VideoCapture(0)
pointx = [0,0,0,0]
pointy = [0,0,0,0]
i=0
while (1):
    imgresp = urllib.request.urlopen(url)
    imgnp = np.array(bytearray(imgresp.read()), dtype=np.uint8)
    frame = cv2.imdecode(imgnp, -1)
    plot = np.zeros((frame.shape[0], frame.shape[1], 3), dtype="uint8")

    blr = cv2.GaussianBlur(frame, (15, 15), 0)
    gray = cv2.cvtColor(blr, cv2.COLOR_BGR2GRAY)
    (t, binImg) = cv2.threshold(gray, 150, 170, cv2.THRESH_BINARY_INV)
    cnts, hrchy = cv2.findContours(binImg, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    n = len(cnts) - 1
    cnts = sorted(cnts, key=cv2.contourArea, reverse=False)[:n]
    if len(cnts) > 0:
        print(len(cnts))
    for c in cnts:
        hull = cv2.convexHull(c)
        # cv2.drawContours(plot, [hull], 0, (0, 255, 0), 3)
        # cv2.drawContours(plot, cnts, 0, (0, 255, 0), 3)
    # cnts, hrchy = cv2.findContours(plot, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    try:
        M = cv2.moments(cnts[0])
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        print(cx,cy)
        if i<4:
            pointx[i] = cx
            pointy[i] = cy
            tm.sleep(0.8)
            i=i+1
        print(pointx,pointy)
        cv2.circle(plot,(cx,cy),3,(0,0,255),2)
    except:
        pass
    if i >= 2:
        for j in range(0,3):
            cv2.line(plot, (pointx[j], pointy[j]), (pointx[j+1], pointy[j+1]), (0, 255, 0), 2)
        cv2.line(plot, (pointx[0], pointy[0]), (pointx[3], pointy[3]), (0, 255, 0), 2)
    cv2.imshow("black", plot)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        exit(0)
    # print(r,g,b,noOfcountors)
cv2.destroyAllWindows()
cap.release()