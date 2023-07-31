import requests

print("***********:: You Can See The Weather Of City ::***********")

# my api key
api_key = "601e31544240aa6c43f35135f3037e27"

# user enter city name
user_city_name = input("_Enter Your City Name => ")

# URL
basic_URL = f"https://api.openweathermap.org/data/2.5/weather?units=metric&appid="

# complete url
complete_URL = basic_URL + api_key + "&q=" + user_city_name

response = requests.get(complete_URL).json()

# Check if the request was successful (status code 200)
if response["cod"] == 200:
    # Convert the temperature from Kelvin to Celsius
    print(f"Temperature: {response['main']['temp']}° C")
else:
    # Handle the case of an invalid city name
    print("Invalid city name. Please check the city name and try again.")



