import folium
import pandas

data= pandas.read_csv("Volcanoes.txt")
dataLon= list(data["LON"])
dataLat=list(data["LAT"])
dataName=list(data["NAME"])
elev=list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map([40.043811, -107.378125])

fgv = folium.FeatureGroup(name="Volcanoes")

#para varias coordenadas
for lt, ln , Name, el in zip(dataLat,dataLon,dataName,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius = 6, popup=Name+" altura "+str(el)+" m", 
                               fill_color=color_producer(el), color= 'dark',fill=True, fill_opacity=0.7 ))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r',encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']< 10000000
                                                      else 'orange' if 10000000 <= x['properties']['POP2005']<20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("mapVolcan.html")






''' anterior for
for lt, ln , Name, el in zip(dataLat,dataLon,dataName,elev):
    fg.add_child(folium.Marker(location=[lt,ln], popup=Name+" altura "+str(el)+" m", icon=folium.Icon(color=color_producer(el))))


    '''
