# Web Map Application

"""
Produces an HTML File that Displays a Map with Three Layers:
    Base Layer (Map Itself)
    Circle Marker Layer (Elevations of Some Volcanoes in the U.S.A.)
    GeoJSON Polygon Layer (Populations of Some Countries)

Latter Two Layers can be Toggled On/Off
"""

# Import Modules
import folium
import pandas



# Choose Color based on Elevation to Represent Volcanoes
def choose_color(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation <= 3000:
        return "orange"
    else:
        return "red"



# Create DataFrame object from CSV File
# Collect Latitude, Longitude, and Elevations
data = pandas.read_csv("volcanoes_usa.csv")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])



# Open JSON File
file = open("countries.json", "r", encoding = "utf-8-sig")



# Create Map object
map = folium.Map(location = [40.758936, -73.985099], zoom_start = 5, tiles = "Mapbox Bright")



# Create Feature Group for Circle Marker Layer (Volcano Elevation)
# Add Each Volcano as a Child to Feature Group
markerFeatureGroup = folium.FeatureGroup(name = "Volcano Elevation: Circle Marker Layer")
for lt, ln, el in zip(lat, lon, elev):
    markerFeatureGroup.add_child(folium.CircleMarker(location = [lt, ln], radius = 6, popup = "Elevation: " + str(el) + "m", fill_color = choose_color(el), color = "grey", fill = True, fill_opacity = 0.85))



# Create Feature Group for GeoJSON Polygon Layer (Country Population)
# Add Each Country as a Child to Feature Group
polygonFeatureGroup = folium.FeatureGroup(name = "Country Population: GeoJSON Polygon Layer")
lbd = lambda feature: {"fillColor": "green" if feature["properties"]["POP2005"] < 10000000
        else "orange" if 10000000 <= feature["properties"]["POP2005"] <= 20000000
        else "red"}
polygonFeatureGroup.add_child(folium.GeoJson(data = file.read(), style_function = lbd))



# Add Feature Groups as Children to Map object
map.add_child(markerFeatureGroup)
map.add_child(polygonFeatureGroup)

# Add Feature that Toggles On/Off Feature Groups as a Child to Map object
map.add_child(folium.LayerControl())

# Save Map object as an HTML File
map.save("map.html")



# Close JSON File
file.close()
