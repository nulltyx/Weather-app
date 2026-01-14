import requests

url = "https://my.meteoblue.com/packages/basic-1h_basic-day_sunmoon"  #link where all the data is
params = {
    "apikey": "", #yur key
    "lat": xxx,  #latitude of your location
    "lon": xxx,   #longitude of your location
    "asl": xxx,  #idk
    "format": "json"   #format
}

response = requests.get(url, params=params)
data = response.json()

times = data["data_1h"]["time"]   #times is what is in data_1h (the like first list) the time is like what specifically im looking for
temps = data["data_1h"]["temperature"]   #same thing but with temperatures
pairs = times, temps   #just makes it easier to print
print(pairs)  #prints dat hoe