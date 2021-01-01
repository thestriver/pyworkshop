import requests

api_url = "http://shibe.online/api/shibes"
params = {
    "count": 10
}

response = requests.get(api_url, params=params)
print(f"The response to the api request made is: {response.status_code}")

response_json = response.json()

print(f"Here are the image url gotten from the API request")
for pic_url in response_json:
    print(f"\t {pic_url}")



