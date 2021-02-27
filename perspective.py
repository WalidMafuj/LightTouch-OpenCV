# import the necessary packages
import numpy as np
import cv2

import cv2

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
       print('x = %d, y = %d'%(x, y))




img = cv2.imread("plot1.JPEG")
cv2.circle(img, (90, 34), 5, (0, 0, 255), -1)
cv2.circle(img, (423, 97), 5, (0, 0, 255), -1)
cv2.circle(img, (25, 415), 5, (0, 0, 255), -1)
cv2.circle(img, (482, 439), 5, (0, 0, 255), -1)



pts1 = np.float32([[90, 34], [423, 97], [25, 415], [482, 439]])
pts2 = np.float32([[0, 0], [500, 0], [0, 600], [500, 600]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
cv2.circle(img, (266, 219), 3, (0, 255, 0), 2)
result = cv2.warpPerspective(img,matrix,(500,600))


# cv2.circle(result, (x, y), 3, (0, 255, 0), 2)

cv2.imshow("Image", img)


cv2.imshow("result", result)

cv2.namedWindow("result")
cv2.setMouseCallback('result', onMouse)

cv2.waitKey(0)
cv2.destroyAllWindows()