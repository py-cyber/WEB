import requests
from Samples.mapapi_PG import show_map

map_request = "http://static-maps.yandex.ru/1.x/?ll=37.622513,55.753220&spn=0.25,0.25&l=map"
response = requests.get(map_request)
location = "ll=30.097431,59.908131&spn=0.2,0.2"

points = [
    "29.914783,59.891574",
    "30.105881,59.944074",
    "30.237944,59.916487",
    "30.266268,59.919073",
    "30.275489,59.930952",
    "30.310165,59.941203"
]
points = ",".join(points)
points_param = f"pl={points}"
show_map(location, "map", add_params=points_param)
