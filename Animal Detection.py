import cv2, time, pandas
import numpy as np
from datetime import datetime
static_back = None
motion_list = [ None, None ]
time = []
df = pandas.DataFrame(columns = ["Start", "End"])
video = cv2.VideoCapture(0)
  
while True:
    check, frame = video.read()
    motion = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
  
    if static_back is None:
        static_back = gray
        continue
    diff_frame = cv2.absdiff(static_back, gray)
    thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)
    cnts,_ = cv2.findContours(thresh_frame.copy(), 
                       cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  
    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        motion = 1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    motion_list.append(motion)
    motion_list = motion_list[-2:]
    if motion_list[-1] == 1 and motion_list[-2] == 0:
        time.append(datetime.now())
  
    if motion_list[-1] == 0 and motion_list[-2] == 1:
        time.append(datetime.now())
  
    key = cv2.waitKey(1)

    if key == ord('q'):
        if motion == 1:
            time.append(datetime.now())
        break

for i in range(0, len(time), 2):
    df = df.append({"Start":time[i], "End":time[i + 1]}, ignore_index = True)
df.to_csv("Time_of_movements.csv")
  
def distance_to_camera(knownWidth, focalLength, perWidth):
	return (knownWidth * focalLength) / perWidth

KNOWN_DISTANCE = 50.00
KNOWN_WIDTH = 45.00
IMAGE_PATHS = ["intial Section.png",]

image = cv2.imread(IMAGE_PATHS[0])
marker = cnts(image)
focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH
for imagePath in IMAGE_PATHS:
	image = cv2.imread(imagePath)
	marker = cnts(image)
	d = distance_to_camera(KNOWN_WIDTH, focalLength, marker[1][0])
	box = np.int0(cv2.cv.BoxPoints(marker))
	cv2.drawContours(image, [box], -1, (0, 255, 0), 2)
	cv2.putText(image, "%.2fft" % d,
		(image.shape[1] - 200, image.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
		2.0, (0, 255, 0), 3)
	cv2.imshow("image", image)
	cv2.waitKey(0)

if d<25.0:
    cv2.waitKey(3000)
    if d<15.0:
        cv2.waitkey(2200)
        if d < 5.00:
            Ultrasonic Sound producer (High,900db,600000ms )



 
