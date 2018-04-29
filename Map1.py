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

fg = folium.FeatureGroup(name='My Map')


for lt, ln, el in zip(lat,lon,elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius= 6, popup=(str(el)), fill_color=color_pick(el), color='grey', fill_opacity=0.7, fill=True))

map.add_child(fg)

map.save('map1.html')
