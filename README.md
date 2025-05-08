# ClimateRoute

ClimateRoute is a Python-based tool designed to process GPX route files and fetch weather data for points along the route. It provides a visualization of the route along with weather information at sampled locations, making it useful for outdoor enthusiasts, travelers, or anyone planning a route-based activity.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ClimateRoute.git
   cd ClimateRoute
   ```

2. Install the required Python libraries:
     ```
     pip3 install -r requirements.txt
     ```

3. Create a configuration file (config.json) with your API details:
     ```json
     {
             "API_KEY": "your_openweather_api_key",
             "WEATHER_API_URL": "openweatherapi.org"
     }
     ```
     Note - [Openweather's](https://openweathermap.org/) api key is required and a free version is also available.
     
4. Place your gpx file in the project directory.

## Usage

Run the script with the following command:
```
cd src
python3 climateRoute.py --config config.json --gpx route.gpx
```
