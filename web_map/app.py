import folium
import pandas

def choose_color(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation <= 3000:
        return "orange"
    else:
        return "red"

data = pandas.read_csv("volcanoes_usa.csv")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location = [40.758936, -73.985099], zoom_start = 10, tiles = "Mapbox Bright")

featureGroup = folium.FeatureGroup(name = "Map")

for lt, ln, el in zip(lat, lon, elev):
    featureGroup.add_child(folium.CircleMarker(location = [lt, ln], radius = 6, popup = "Elevation: " + str(el) + "m", fill_color = choose_color(el), color = "grey", fill = True, fill_opacity = 0.85))

map.add_child(featureGroup)

map.save("map.html")
