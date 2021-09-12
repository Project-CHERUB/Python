# from https://www.pyimagesearch.com/2018/07/23/simple-object-tracking-with-opencv/
class TrackableObject:
	def __init__(self, objectID, centroid):
		# store the object ID, then initialize a list of centroids
		# using the current centroid
		self.objectID = objectID
		self.centroids = [centroid]

		# initialize a boolean used to indicate if the object has
		# already been counted or not
		self.counted = False

		# initialize an integer corresponding to if the person is 
		# in an entry
		self.in_entry = False
