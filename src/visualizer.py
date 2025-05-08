import matplotlib.pyplot as plt
import webbrowser
import folium
import gpxpy
import os

def draw_route(wmap, coords):
    """
    Draws a route on a given map using a list of coordinates.

    Args:
        wmap (folium.Map): The map object where the route will be drawn.
        coords (list of tuple): A list of (latitude, longitude) tuples representing the route.

    Returns:
        None
    """
    folium.PolyLine(coords, color="blue", weight=3).add_to(wmap)

def draw_text(wmap, data):
    """
    Adds text markers to a folium map with custom styling.
    This function takes a folium map object and a list of data points, where each data point
    contains latitude, longitude, and a text label. It places styled text markers at the 
    specified locations on the map.
    Args:
        wmap (folium.Map): The folium map object to which the text markers will be added.
        data (list of tuples): A list of tuples, where each tuple contains:
            - lat (float): Latitude of the marker.
            - lon (float): Longitude of the marker.
            - txt (str): The text to display at the marker location.
    Returns:
        None
    """
    
    for lat, lon, txt in data:
        folium.Marker(
            location=[lat, lon],
            icon=folium.DivIcon(html=f"""
                <div style="font-size: 14px; background-color: white; border: 1px solid black; 
                padding: 6px 10px; border-radius: 6px; box-shadow: 2px 2px 6px rgba(0,0,0,0.3);
                white-space: normal; word-wrap: break-word; display: inline-block;">
                {txt}</div>""")).add_to(wmap)

def draw_route_and_text(coords, weather_data):
        """
        Generates an interactive map displaying a route and associated weather data.

        This function creates a folium map centered at the first coordinate in the 
        provided list of coordinates. It draws the route on the map, overlays weather 
        information as text, saves the map to an HTML file, and opens it in the default 
        web browser.

        Args:
            coords (list of tuple): A list of latitude and longitude pairs representing 
                the route to be drawn on the map.
            weather_data (dict): A dictionary containing weather information to be 
                displayed on the map.

        Returns:
            None
        """
        wmap = folium.Map(location=coords[0], zoom_start=13)
        draw_route(wmap, coords)
        draw_text(wmap, weather_data)
        map_file = "gpx_weather_map.html"
        wmap.save(map_file)
        webbrowser.open('file://' + os.path.realpath(map_file))