import requests

clave = "3d2159b8"
url = "http://www.omdbapi.com/?apikey=" + clave
r = requests.get(url, {"s" : "The Matrix", "type" : "movie"})

print(r.json())
r = requests.get(url, {"i" : "tt0133093", "type" : "movie"})
print(r.json())

r = requests.get(url, {"t" : "The Matrix", "type" : "movie"})
print(r.json())