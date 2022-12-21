from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my-custom-application")
location = geolocator.geocode("my location")
print(location.latitude, location.longitude)

#python testFR.py