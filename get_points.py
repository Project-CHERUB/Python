from shapely.geometry import Point, Polygon
import numpy as np
import cv2
import time
import imutils

def get_points(entry_file_path):
	entrances = []
	entry_file = open(entry_file_path)
	entrance = []
	lines = entry_file.readlines()
	lines = set(lines)
	for line in lines:
		line = line[2:-3]
		point_arr = line.split("], [")
		for coord_str in point_arr:
			coords = coord_str.split(", ")
			entrance.append([int(coords[0]),int(coords[1])])
		entrances.append(Polygon(entrance))
		entrance = []
	return entrances