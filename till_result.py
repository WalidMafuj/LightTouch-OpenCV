import cv2
import numpy as np
import time as tm
import urllib.request
import os


def listToString(s):
    str1 = ""
    for ele in s:
        str1 += str(ele)
        str1 += ' '
    return str1

url = "http://192.168.0.3:8080/shot.jpg"
cap = cv2.VideoCapture(0)

x=1920
y=767
pointx = [0,0,0,0]
pointy = [0,0,0,0]
i=0
file1 = open("Cal.txt", "w")



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
            if i ==3:
                point_x = listToString(pointx)
                point_y = listToString(pointy)
                file1.write(point_x)
                file1.write(point_y)
                # file2.write(point_y)
        print(pointx,pointy)

        cv2.circle(plot,(cx,cy),3,(0,0,255),2)
    except:
        pass
    # if i >= 2:
    #     for j in range(0,3):
    #         cv2.line(plot, (pointx[j], pointy[j]), (pointx[j+1], pointy[j+1]), (0, 255, 0), 2)
    #     cv2.line(plot, (pointx[0], pointy[0]), (pointx[3], pointy[3]), (0, 255, 0), 2)

    pts1 = np.float32([[pointx[0], pointy[0]], [pointx[1], pointy[1]], [pointx[2], pointy[2]], [pointx[3], pointy[3]]])
    pts2 = np.float32([[0,0],[0, y],[x, 0], [x, y]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(frame, matrix, (x, y))
    if i == 0:
        cv2.circle(result, (10, 10), 3, (0, 0, 255), 2)
    if i == 1:
        cv2.circle(result, (10, frame.shape[0] - 10), 3, (0, 0, 255), 2)
    if i == 2:
        cv2.circle(result, (frame.shape[0] -10 , 10), 3, (0, 0, 255), 2)
    if i == 3:
        cv2.circle(result, (frame.shape[0] - 10 , frame.shape[0] -10 ), 3, (0, 0, 255), 2)

    # cv2.imshow("plot", plot)
    cv2.imshow("frame", frame)
    cv2.imshow("result", result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        exit(0)
    if cv2.waitKey(1) & 0xFF == ord('m'):
        exit(0)
    if cv2.waitKey(1) & 0xFF == ord('r'):
        pointx = [0, 0, 0, 0]
        pointy = [0, 0, 0, 0]
        i = 0
        file1 = open("Cal.txt", "w")
    # print(r,g,b,noOfcountors)
cv2.destroyAllWindows()
cap.release()