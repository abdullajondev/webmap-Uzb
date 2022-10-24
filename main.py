


from turtle import color, fillcolor
import pandas
import folium

map = folium.Map(location=[41.311081, 69.240562], zoom_start=6, tiles="Stamen Terrain")
fgv = folium.FeatureGroup(name= "Volcanoes")
fgp = folium.FeatureGroup(name="Population")

data = pandas.read_excel("file.xlsx", sheet_name=0)

lat = list(data["Latitude"])
lon = list(data["Longitude"])
city_name = list(data["Name"])


    

for lat, lon, name in zip(lat, lon, city_name):
    fgv.add_child(folium.Marker(location=[lat, lon], popup=name, icon=(folium.Icon(color="green"))))

fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
style_function=lambda x: {"fillColor": "yellow" if x["properties"]["POP2005"] < 10000000 else "red" 
if 10000000 <= x["properties"]["POP2005"] < 50000000  else "orange"}))  

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
