import folium
import pandas

map = folium.Map(location=[45.58, -99.09], zoom_start=6, tiles='Mapbox Bright')
data = pandas.read_csv('vol.txt') # [8] and [9] have lat and lon.
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

def color_pick(height):
    if height < 1500:
        color = 'green'
    elif 1500 <= height < 2500:
        color = 'orange'
    else:
        color = 'red'
    return color

fgv = folium.FeatureGroup(name='Volcanoes')


for lt, ln, el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius= 6, popup=(str(el)), fill_color=color_pick(el), color='grey', fill_opacity=0.7, fill=True))

fgpop = folium.FeatureGroup(name='Population')


fgpop.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'red' if x['properties']['POP2005'] < 100000
else 'orange' if 1000000 <= x['properties']['POP2005'] < 30000000 else 'green' }))

map.add_child(fgv)
map.add_child(fgpop)
map.add_child(folium.LayerControl())

map.save('map1.html')
