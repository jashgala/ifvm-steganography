#### Demonstration of frame splitting using OpenCV in Python #### 

import cv2
import numpy

# droopy.mp4 is the video file MP4, 4 sec, 88 frames downlaoded from YouTube using 'savefromnet'
cap = cv2.VideoCapture('droopy.mp4')

# The following loop extractsthe first fifty frames from the mp4 video. Each frame is an openCV image (array).
for i in  range(0,50):
        ret, frame = cap.read()
        cv2.imwrite('frame' + str(i) + '.png', frame)
        print 'wrote frame ' + str(i)

print "Done with frame extraction!"
