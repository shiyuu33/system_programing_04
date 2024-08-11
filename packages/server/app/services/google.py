
import googlemaps
import config


class Google:
    def __init__(self) -> None:
        self.client = googlemaps.Client(config.API_DIRECTIONS_KEY)
    def get_location(self, start_place: str, end_place: str) -> tuple[dict[str, float], dict[str, float]]:
        direction_result = self.client.directions(start_place, end_place)
        data_result = direction_result[0]
        data_legs = data_result["legs"][0]
        start_location: dict[str, float] = data_legs["end_location"]
        end_location: dict[str, float]  = data_legs["end_location"]
        return start_location, end_location