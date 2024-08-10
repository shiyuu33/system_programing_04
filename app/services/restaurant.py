import requests
import config

class Restaurant:
    def __init__(self) -> None:
        self.key = config.API_RESTAURANT_KEY
        self.url = config.API_RESTAURANT_URL
    def get_restaurant_list(self, lat: str, lng: str):
        params = {
        'key': self.key,
        'lat': lat,
        'lng': lng,
        'order': 4,
        'format':'json',
        }
        response = requests.get(f"{self.url}", params)
        data = response.json()
        return data