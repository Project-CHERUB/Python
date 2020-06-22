from shapely.geometry import Point, Polygon
import numpy as np
import cv2
import time
import imutils
import argparse
from get_points import get_points

def setup_entrances(entrance_file_path, video_path):
	points = []	

	cap = cv2.VideoCapture(video_path)
	i = 10
	j = 10
	increment = 7
	ret, frame_orig = cap.read()

	entrances_file = open(entrance_file_path,"r+") 

	entrances = entrances_file.readlines()
	
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
		if key == ord('u'):
			points = points[:-1]

		polycoords = np.int32(points)
		cv2.polylines(frame, [polycoords], len(polycoords)>3, (0,255,0), thickness=2)

		if key == ord('f'):
			entrances.append(str(points)+'\n')
			points = []

		cv2.imshow('frame',frame)
		if key & 0xFF == ord('q'):
			break

	cap.release()
	cv2.destroyAllWindows()
	entrances_file.truncate(0)
	entrances_file.writelines(entrances)

def delete_entrance(entrance_file_path, video_path):
	cap = cv2.VideoCapture(video_path)
	ret, frame_orig = cap.read()

	entrances_file = open(entrance_file_path,"a")

	entrances = get_points(entrance_file_path)
	entrances = entrances
	for i in range(len(entrances)):
		coords = entrances[i].exterior.coords[:-1]
		for j in range(len(coords)):
			coords[j] = [int(coords[j][0]),int(coords[j][1])]
		entrances[i] = coords

	if len(entrances)>0:
		index = 0

		while True:
			frame = frame_orig	
			frame = imutils.resize(frame, width=500)
			key = cv2.waitKey(1)

			if key == ord('n'):
				index += 1
				if index % len(entrances) == 0:
					index = 0
				# print(index)
			if key == ord('d'):
				del entrances[index]
				if len(entrances) == 0:
					break
				if index == len(entrances):
					index = 0

			for i in range(len(entrances)):
				polycoords = np.int32(entrances[i])
				if (i==index):
					cv2.polylines(frame, [polycoords], len(polycoords)>3, (0,0,255), thickness=2)
				else:
					cv2.polylines(frame, [polycoords], len(polycoords)>3, (0,255,0), thickness=2)

			cv2.imshow('frame',frame)
			if key & 0xFF == ord('q'):
				break

		cap.release()
		cv2.destroyAllWindows()
		entrance_strs = []
		for entrance in entrances:
			entrance_strs.append(str(entrance)+"\n")
		entrances_file.truncate(0)
		entrances_file.writelines(entrance_strs)

# setup_entrances("entrances.txt","StoreEntrance.mp4")
# delete_entrance("entrances.txt","StoreEntrance.mp4")