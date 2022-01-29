import sys

from Samples.geocoder import geocode

cities = sys.argv[1:]
southest = 100
southest_city = ''
for city in cities:
    toponym = geocode(city)
    toponym_coodrinates = float(toponym["Point"]["pos"].split()[1])
    if toponym_coodrinates < southest:
        southest = toponym_coodrinates
        southest_city = city
print(southest_city)
