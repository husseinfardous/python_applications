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

file = open("countries.json", "r", encoding = "utf-8-sig")

map = folium.Map(location = [40.758936, -73.985099], zoom_start = 5, tiles = "Mapbox Bright")

markerFeatureGroup = folium.FeatureGroup(name = "Volcano Elevation: Circle Marker Layer")
for lt, ln, el in zip(lat, lon, elev):
    markerFeatureGroup.add_child(folium.CircleMarker(location = [lt, ln], radius = 6, popup = "Elevation: " + str(el) + "m", fill_color = choose_color(el), color = "grey", fill = True, fill_opacity = 0.85))

polygonFeatureGroup = folium.FeatureGroup(name = "Country Population: GeoJSON Polygon Layer")
lbd = lambda feature: {"fillColor": "green" if feature["properties"]["POP2005"] < 10000000
        else "orange" if 10000000 <= feature["properties"]["POP2005"] <= 20000000
        else "red"}
polygonFeatureGroup.add_child(folium.GeoJson(data = file.read(), style_function = lbd))

map.add_child(markerFeatureGroup)
map.add_child(polygonFeatureGroup)
map.add_child(folium.LayerControl())
map.save("map.html")

file.close()
