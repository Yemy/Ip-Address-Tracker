import folium
import geocoder
# import socket    


# host_name = socket.gethostname()    
# IPAddress = socket.gethostbyname(host_name)    
# print("Your Computer Name is:" + host_name)    
# print("Your Computer IP Address is:" + IPAddress) 

g = geocoder.ip('172.29.32.1')

my_addr = g.latlng

my_map1 = folium.Map(location=my_addr, zoom_start=12)

folium.CircleMarker(location=my_addr, radius=20, popup="yorkshire").add_to(my_map1)

folium.Marker(my_addr, popup="yorkshire").add_to(my_map1)

my_map1.save('my_map.html')
