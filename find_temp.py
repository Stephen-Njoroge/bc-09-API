import time, urllib3, json
from tqdm import * #graphic counter module
for i in tqdm(range(5)): 
	time.sleep(0.5)
def find_weather(city):
	"""
	This application finds the weather of a given area,
	and the average temaparature.

	"""

	try:
		http = urllib3.PoolManager()
		response = http.request('GET', 
			'http://api.openweathermap.org/data/2.5/weather', 
			fields ={
			'q':city, 
			'units':'metric', 
			"appid": "2bc3e79bb974a007818864813f53fd35"
			})  
		parsed_data = json.loads(response.data.decode('utf-8'))
		
		
		return ("\t{}\t{}\t{}").format((parsed_data['name']).ljust(10),(str(parsed_data["main"]["temp"])).ljust(10), parsed_data["weather"][0]["description"])

	except Exception as e:
		print (e)

	
print ("\t{}\t{}\t{}").format("City", "Temperature".ljust(15), "Description".ljust(20))
print("="*45)

cities = [
"Nairobi", "Kisumu", "Mombasa", "New York", "Portmore", "Kingstone", "California", "Kampala", "Arusha",
"Dodoma", "Nakuru", "Kigali"
]

for city in cities:
	print (find_weather(city))