from shapely.geometry import Point, Polygon
import numpy as np
import cv2
import time
import imutils
import argparse

def setup_entrances(entrance_file_path, video_path):
	points = []	

	cap = cv2.VideoCapture(video_path)
	i = 0
	j = 0
	increment = 7
	ret, frame_orig = cap.read()

	entrances_file = open(entry_file_path,"w+") 

	while True:
		frame = frame_orig	
		frame = imutils.resize(frame, width=500)
		cv2.circle(frame, (i,j), 3, (255,255,0), thickness=2)
		h, w, _ = frame.shape

		key = cv2.waitKey(1)
		if key == ord('w'):
			j = max(j-increment,0)
		if key == ord('a'):
			i = max(i-increment,0)
		if key == ord('s'):
			j = min(j+increment,h)
		if key == ord('d'):
			i = min(i+increment,w)

		if key == ord('p'):
			points.append([i,j])
		if key == ord('r'):
			points = points[:-1]

		polycoords = np.int32(points)
		cv2.polylines(frame, [polycoords], len(polycoords)>3, (0,255,0), thickness=2)

		cv2.imshow('frame',frame)
		if key & 0xFF == ord('q'):
			break

	cap.release()
	cv2.destroyAllWindows()
	print(points)
	entrances_file.write(str(points))
