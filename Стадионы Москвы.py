import requests
from mapapi_PG import show_map

map_request = "http://static-maps.yandex.ru/1.x/?ll=37.622513,55.753220&spn=0.25,0.25&l=map"
response = requests.get(map_request)
moscow = "ll=37.622513,55.753220&spn=0.25,0.25"
alf = {
    'Spartak': "37.435250,55.818103",
    'Dinamo': "37.558212,55.789704",
    'Lujniki': "37.551932,55.717934"
}
points = "~".join([pt for pt in alf.values()])
points_param = f"pt={points}"
show_map(moscow, "map", add_params=points_param)
