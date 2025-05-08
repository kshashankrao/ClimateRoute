import visualizer 

import argparse
import requests
import gpxpy
import folium
import json
import time

"""
A class to process a GPX route and fetch weather data for points along the route.
"""
class climateRoute:
    def __init__(self, config_path, gpx_file_path):
        """
        Initializes the climateRoute object.
        Args:
        config_path (str): Path to the JSON configuration file containing API details.
        gpx_file_path (str): Path to the GPX file containing the route. 
        """
        self.config = json.load(open(config_path))
        self.API_KEY = self.config["API_KEY"]
        self.WEATHER_API_URL = self.config["WEATHER_API_URL"]
        self.route = self.load_gpx(gpx_file_path)  
        
    def load_gpx(self, gpx_file_path):
        """
        Loads the GPX file and extracts the route points.
        Args:
            gpx_file_path (str): Path to the GPX file.
        Returns:
            list: A list of points (latitude and longitude) from the GPX file.
        """
        with open(gpx_file_path, 'r') as file:
            gpx = gpxpy.parse(file)
            return gpx.tracks[0].segments[0].points

    def get_weather(self, lat, lon):
        """
        Fetches weather data for a given latitude and longitude.
        Args:
            lat (float): Latitude of the location.
            lon (float): Longitude of the location.
        Returns:
            dict: Weather data in JSON format if the request is successful.
            None: If the request fails.
        """
        params = {'lat': lat, 'lon': lon, 'appid': self.API_KEY, 'units': 'metric'}
        response = requests.get(self.WEATHER_API_URL, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch weather for ({lat}, {lon}) - HTTP {response.status_code}")
            return None
    
    def run(self):
        """
        Processes the route, fetches weather data at sampled points, and visualizes the route.
        """
        coords = []
        weather_labels = []

        for i, point in enumerate(self.route):
            coords.append((point.latitude, point.longitude))
            sample_rate = len(self.route) // 10
        
            if i % sample_rate == 0:
                weather = self.get_weather(point.latitude, point.longitude)
                label = f"{weather['weather'][0]['description']} {weather['main']['temp']}°C"
                weather_labels.append((point.latitude, point.longitude, label))
                time.sleep(1)  

        if not coords:
            print("No coordinates found.")
            return

        visualizer.draw_route_and_text(coords, weather_labels)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Process a GPX route and fetch weather data.")
    parser.add_argument('--config', type=str, default='climateRoute.json', help='Path to the JSON configuration file (default: climateRoute.json)')
    parser.add_argument('--gpx', type=str, default='route.gpx', help='Path to the GPX file (default: route.gpx)')
    args = parser.parse_args()

    cr = climateRoute(args.config, args.gpx)
    cr.run()
