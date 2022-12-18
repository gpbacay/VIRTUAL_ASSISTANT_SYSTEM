from time import time
from numpy import number
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

Mobile_No = input("Enter your phone number: ")
Mobile_No = phonenumbers.parse(Mobile_No)

Carrier_Name = carrier.name_for_number(Mobile_No, "en")
time = timezone.time_zones_for_number(Mobile_No)
Location = geocoder.description_for_number(Mobile_No, "en")
Country = geocoder.country_name_for_number(Mobile_No, "en")


print(Carrier_Name)
print(time)
print(Location)
print(Country)

#python MobileTracker.py