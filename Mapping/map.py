import folium
map = folium.Map([-34.658026535298525, -58.581487318758825])

fg = folium.FeatureGroup(name="My Map")

#para una coodenada
#fg.add_child(folium.Marker(location=[-34.658026535298525, -58.581487318758825], popup="My Location", icon=folium.Icon(color='green')))

#para varias coordenadas
for coordinates in [[-34.658026535298525, -58.581487318758825],[-33.658026535298525, -57.581487318758825]]:
    fg.add_child(folium.Marker(location=coordinates, popup="My Location", icon=folium.Icon(color='green')))


map.add_child(fg)
map.save("map.html")


     
'''  
    html = """
    Volcano name:<br>
    <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
    Height: %s m
    """
     
    map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Mapbox Bright")
    fg = folium.FeatureGroup(name = "My Map")
     
    for lt, ln, el, name in zip(lat, lon, elev, name):
        iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
        fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = "green")))
     
    map.add_child(fg)
    map.save("Map_html_popup_advanced.html")'''