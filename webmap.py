import folium
import pandas

data = pandas.read_csv('datas/Volcanoes.txt')
#create an instance of map object
map = folium.Map(location=[data['LAT'].mean(), data['LON'].mean()], zoom_start=4)
print(dir(map))


def color(el):
    if el in range(int(min(data['ELEV'])), int(max(data['ELEV'])) - int(min(data['ELEV']))//3):
        return 'red'
    elif el in range(int(min(data['ELEV'])), int(max(data['ELEV'])) - int(min(data['ELEV']))//3):
        return 'black'
    else:
        return 'blue' 

#get lat and lon
for lat, lon, name, loc, el in zip(data['LAT'], data['LON'], data['NAME'], data['LOCATION'], data['ELEV']):
    folium.Marker([lat, lon], popup= f'{name}\n{loc}', icon= folium.Icon(color=color(el))).add_to(map)
    #print(lat, lon)





map.save('test.html')

