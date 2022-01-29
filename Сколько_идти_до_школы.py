import sys
from Samples.distance import lonlat_distance
from Samples.geocoder import get_coordinates

print(lonlat_distance(get_coordinates(sys.argv[1]), get_coordinates(sys.argv[2])))
