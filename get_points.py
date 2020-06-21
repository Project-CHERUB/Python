from shapely.geometry import Point, Polygon
import numpy as np
import cv2
import time
import imutils

def get_points(entry_file_path):
	entrances = []
	entry_file = open(entry_file_path)
	entrance = []
	points_str = entry_file.read()
	points_str = points_str[2:-2]
	point_arr = points_str.split("], [")
	for coord_str in point_arr:
		coords = coord_str.split(", ")
		entrance.append([int(coords[0]),int(coords[1])])
	entrances.append(Polygon(entrance))
	return entrances