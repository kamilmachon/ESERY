import cv2
import numpy as np



# def nothing(srsl_nothing):
#     pass
ur = 255
ub = 130
lr = 115
lb = 92

cap = cv2.imread('hand.jpg', 1)
x, y = cap.shape[1], cap.shape[0]

ycbcr = cv2.cvtColor(cap, cv2.COLOR_BGR2YCrCb)
upper_threshold = np.array([255, ur, ub], dtype = np.uint8)
lower_threshold = np.array([0, lr, lb], dtype = np.uint8)
binary = cv2.inRange(ycbcr, lower_threshold, upper_threshold)
binary = cv2.medianBlur(binary, 5)

#64x64 zapis
resized = cv2.imread('hand.jpg', 1)
resized = resized[0:y, x/2 - y/2: x/2 + y/2]
resized = cv2.resize(resized, (64, 64))
cv2.imwrite("hand_resized.ppm", resized)

cap = binary
cv2.waitKey(0)
for i in range(cap.shape[0]):
    for j in range(cap.shape[1]):
        if(i < 10 or i > cap.shape[0] - 10 or j < 10 or j > cap.shape[1] - 10):
            cap[i, j] = 0

# cap = cv2.medianBlur(cap, 5);

m00 = 0
m10 = 0
m01 = 0

for i in range(cap.shape[0]):
    for j in range(cap.shape[1]):
        m00 += cap[i,j]
        m10 += i*cap[i,j]
        m01 += j*cap[i,j]

x = int(float(m10)/float(m00))
y = int(float(m01)/float(m00))
print x,y

cap = cv2.cvtColor(cap, cv2.COLOR_GRAY2BGR)
#dobre wspolrzedne
cv2.circle(cap, (y,x), 10, (0, 0, 255), 1)
cv2.line(cap, (0, x), (cap.shape[1], x), (0, 0, 255), 1)
cv2.line(cap, (y, 0), (y, cap.shape[0]), (0, 0, 255), 1)

# odwrotnie wspolrzedne
# cv2.circle(cap, (x,y), 10, (0, 255, 0), 1)
# cv2.line(cap, (0, y), (cap.shape[1], y), (0, 255, 0), 1)
# cv2.line(cap, (x, 0), (x, cap.shape[0]), (0, 255, 0), 1)

cv2.imshow("mask", cap)
# cv2.imshow("gowno", img)
cv2.waitKey(0)



#binary
######################################################################################################################

#
#
# cv2.namedWindow('control panel')
# cv2.createTrackbar('Upper r', 'control panel', ur, 255, nothing)
# cv2.createTrackbar('Upper b', 'control panel', ub, 255, nothing)
#
# cv2.createTrackbar('Lower r', 'control panel', lr, 255, nothing)
# cv2.createTrackbar('Lower b', 'control panel', lb, 255, nothing)
#
# while True:
#
#
#
#     cv2.imshow('start', cap)
#
    # ycbcr = cv2.cvtColor(cap, cv2.COLOR_BGR2YCrCb)
#     cv2.imshow('ycbcr', ycbcr)
#
#     upper_threshold = np.array([255, cv2.getTrackbarPos("Upper r", "control panel"), cv2.getTrackbarPos("Upper b", "control panel")], dtype = np.uint8)
#     lower_threshold = np.array([0, cv2.getTrackbarPos("Lower r", "control panel"), cv2.getTrackbarPos("Lower b", "control panel")], dtype = np.uint8)
#
#     binary = cv2.inRange(ycbcr, lower_threshold, upper_threshold)
#     binary = cv2.medianBlur(binary, 5)
#
#     cv2.imshow('binary', binary)
#
#     k = cv2.waitKey(2)
#     if k == 27:
#         break












cv2.destroyAllWindows()
