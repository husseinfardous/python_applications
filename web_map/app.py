import folium
import pandas

data = pandas.read_csv("volcanoes_usa.csv")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location = [40.758936, -73.985099], zoom_start = 10, tiles = "Mapbox Bright")

featureGroup = folium.FeatureGroup(name = "Map")

for lt, ln, el in zip(lat, lon, elev):
    featureGroup.add_child(folium.Marker(location = [lt, ln], popup = "Elevation: " + str(el) + "m", icon = folium.Icon(color = "red")))

map.add_child(featureGroup)

map.save("map.html")
