from fastapi import FastAPI
from typing import List
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from difflib import get_close_matches

app = FastAPI()
geolocator =Nominatim(user_agent='moustache property locator')



properties = [
    {"property": "Moustache Udaipur Luxuria", "latitude": 24.57799888, "longitude": 73.68263271},
    {"property": "Moustache Udaipur", "latitude": 24.58145726, "longitude": 73.68223671},
    {"property": "Moustache Udaipur Verandah", "latitude": 24.58350565, "longitude": 73.68120777},
    {"property": "Moustache Jaipur", "latitude": 27.29124839, "longitude": 75.89630143},
    {"property": "Moustache Jaisalmer", "latitude": 27.20578572, "longitude": 70.85906998},
    {"property": "Moustache Jodhpur", "latitude": 26.30365556, "longitude": 73.03570908},
    {"property": "Moustache Agra", "latitude": 27.26156953, "longitude": 78.07524716},
    {"property": "Moustache Delhi", "latitude": 28.61257139, "longitude": 77.28423582},
    {"property": "Moustache Rishikesh Luxuria", "latitude": 30.13769036, "longitude": 78.32465767},
    {"property": "Moustache Rishikesh Riverside Resort", "latitude": 30.10216117, "longitude": 78.38458848},
    {"property": "Moustache Hostel Varanasi", "latitude": 25.2992622, "longitude": 82.99691388},
    {"property": "Moustache Goa Luxuria", "latitude": 15.6135195, "longitude": 73.75705228},
    {"property": "Moustache Koksar Luxuria", "latitude": 32.4357785, "longitude": 77.18518717},
    {"property": "Moustache Daman", "latitude": 20.41486263, "longitude": 72.83282455},
    {"property": "Panarpani Retreat", "latitude": 22.52805539, "longitude": 78.43116291},
    {"property": "Moustache Pushkar", "latitude": 26.48080513, "longitude": 74.5613783},
    {"property": "Moustache Khajuraho", "latitude": 24.84602104, "longitude": 79.93139381},
    {"property": "Moustache Manali", "latitude": 32.28818695, "longitude": 77.17702523},
    {"property": "Moustache Bhimtal Luxuria", "latitude": 29.36552248, "longitude": 79.53481747},
    {"property": "Moustache Srinagar", "latitude": 34.11547314, "longitude": 74.88701741},
    {"property": "Moustache Ranthambore Luxuria", "latitude": 26.05471373, "longitude": 76.42953726},
    {"property": "Moustache Coimbatore", "latitude": 11.02064612, "longitude": 76.96293531},
    {"property": "Moustache Shoja", "latitude": 31.56341267, "longitude": 77.36733331}
]


@app.get("/search",response_model=list[str])
async def search(location:str):

    city_keywords = list({p["property"].split()[-1].lower() for p in properties})
    best_match = get_close_matches(location.lower(), city_keywords, n=1, cutoff=0.6)
    
    if not best_match:
        return []
    try:
        loc = geolocator.geocode(best_match[0])

        if not loc:
            return []
        input_coords = (loc.latitude, loc.longitude)
        nearby = []
        for prop in properties:
            prop_coords = (prop["latitude"], prop["longitude"])
            if geodesic(input_coords, prop_coords).km <= 50:
                nearby.append(prop["property"])
        
        return nearby

    except Exception as e:
        return []



   
