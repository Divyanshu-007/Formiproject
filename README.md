🧠 Initial Thought Process:-
The core idea is to help tele-calling agents by showing nearby Moustache Escapes properties when a customer mentions a location during a call.
So, I focused on the main need:
"Given any input location (city, town, area), show all properties within 50km of that point."

🔍 Breakdown into Manageable Parts:
1. Input Understanding:
Input is a free-form location query (city, area, state).
Needs to be converted to latitude/longitude (using geocoding).
2. Data Setup:
A predefined list of properties with lat/lon values is provided.
Should be loaded into memory or a database (for now, a list is fine).
3. Geocoding the Input:
Use a geocoding service like Nominatim (via geopy) to turn the text query into coordinates.
4. Distance Calculation:
For each property, compute the distance from the input location.
If ≤ 50km, include it in the result.
5. Handling Errors or Edge Cases:
Invalid locations, geocoding failures.
No properties found.
Optional: fuzzy match if geocoding fails.
6. API Design:
A GET endpoint, /search?location=...
Return a list of properties or a message like "no properties found".

1. FastAPI
Why:
Simple, modern, and fast framework for building APIs in Python.
Automatic generation of Swagger UI docs.
Easy to set up and test locally or deploy.

2. geopy Library
Why:
Used to convert human-readable locations to coordinates (Nominatim) and calculate geodesic distances.
Easy to integrate and well-documented.

3. Nominatim Geocoder (geopy.geocoders.Nominatim)
Why:
Free and open-source location geocoding.
Converts the user's location query into latitude and longitude.

4. geopy.distance.geodesic()
Why:
Calculates the great-circle distance (accurate for most travel-related use cases).
Helps in filtering properties within a 50km radius.

5. difflib.get_close_matches()
Why:
Adds a layer of fuzzy matching to handle slight misspellings or partial location names.
Lightweight, built-in Python tool – no need for external dependencies like fuzzywuzzy or RapidFuzz.

6. Notion Page (Property List Source)
Why:
Provides a centralized and structured list of properties.
You copied the relevant property data from this and hardcoded it for testing.

🔍 Problem Details:
Users may type incomplete, misspelled, or vague location queries.
e.g., "udaipr", "near taj mahal", or just "rishikesh".
Direct geocoding sometimes fails or returns incorrect coordinates for vague terms.
This would lead to no results found, even when relevant properties exist nearby.

🛠️ How I Solved It:
1. Fuzzy Matching on Known City Names
Extracted city keywords from all Moustache property names.
Used difflib.get_close_matches() to match user input with these known city keywords.
This ensures the input is cleaned and corrected before geocoding.

2. Reliable Geocoding with Fallback
Once I had a matched city name, used Nominatim (via geopy) to fetch latitude and longitude.
Handled geocoding failures gracefully using a try-except block.

3. Geodesic Distance Filter
Used geopy.distance.geodesic() to accurately calculate real-world distances.
Filtered only those properties that lie within 50 km.

I Would Explore the Following Improvements in future:
1. Replace Fuzzy Matching with a Smarter Location Resolver
2.  Switch to a More Reliable Geocoding API
3.  Move Property Data to a Database
4.  Add Caching for Repeated Locations
5.  Add Ranking or Sorting by Distance
6.  Add Error Handling and Logging
 
Why These Improvements Are Valuable:
Better accuracy = better customer experience
Scalability = easy to maintain and extend
Reliability = smoother usage in production
Performance = faster responses to users


