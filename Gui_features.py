import cv2
import numpy as np

OUTPUT_FOLDER = './output/'
INPUT_FOLDER = './input/'
FPS = 20.0
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(INPUT_FOLDER+'big_buck_bunny.mp4')
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter(OUTPUT_FOLDER+'savevideo.avi', fourcc, FPS, (int(width),int(height)))
if cap.isOpened() == False:
    print 'Open error'
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
    	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	out.write(frame)
   	cv2.imshow('Gray', gray)
    	if cv2.waitKey(1) & 0xFF == ord('q'):
	    break
    else:
	print 'read error'
	break
cap.release()
cv2.destroyAllWindows()


