from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import requests
from datetime import datetime


class WeatherToolInput(BaseModel):
    """Input schema for WeatherTool."""
    location: str = Field(..., description="City name or coordinates (e.g., 'London' or 'lat,lon')")


class WeatherTool(BaseTool):
    name: str = "Weather Forecast Tool"
    description: str = (
        "Provides current weather and 5-day forecast for a specified location. "
        "Use this tool when you need weather information for planning or decision-making. "
        "Input should be a city name (e.g., 'New York') or coordinates."
    )
    args_schema: Type[BaseModel] = WeatherToolInput

    def _run(self, location: str) -> str:
        """
        Fetches weather data for the specified location.
        Uses Open-Meteo API (free, no API key required).
        """
        try:
            # First, geocode the location to get coordinates
            geocode_url = "https://geocoding-api.open-meteo.com/v1/search"
            geocode_params = {
                "name": location,
                "count": 1,
                "language": "en",
                "format": "json"
            }
            
            geo_response = requests.get(geocode_url, params=geocode_params, timeout=10)
            geo_response.raise_for_status()
            geo_data = geo_response.json()
            
            if not geo_data.get("results"):
                return f"Location '{location}' not found. Please check the spelling and try again."
            
            # Extract coordinates
            result = geo_data["results"][0]
            lat = result["latitude"]
            lon = result["longitude"]
            city_name = result["name"]
            country = result.get("country", "")
            
            # Fetch weather data
            weather_url = "https://api.open-meteo.com/v1/forecast"
            weather_params = {
                "latitude": lat,
                "longitude": lon,
                "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m",
                "daily": "weather_code,temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max",
                "timezone": "auto",
                "forecast_days": 6  # Today + 5 days
            }
            
            weather_response = requests.get(weather_url, params=weather_params, timeout=10)
            weather_response.raise_for_status()
            weather_data = weather_response.json()
            
            # Format the response
            output = f"Weather Forecast for {city_name}, {country}\n"
            output += "=" * 50 + "\n\n"
            
            # Current weather
            current = weather_data["current"]
            output += f"CURRENT WEATHER ({current['time']}):\n"
            output += f"  Temperature: {current['temperature_2m']}°C\n"
            output += f"  Humidity: {current['relative_humidity_2m']}%\n"
            output += f"  Wind Speed: {current['wind_speed_10m']} km/h\n"
            output += f"  Conditions: {self._get_weather_description(current['weather_code'])}\n\n"
            
            # 5-day forecast
            output += "5-DAY FORECAST:\n"
            daily = weather_data["daily"]
            
            for i in range(min(6, len(daily["time"]))):
                date = datetime.fromisoformat(daily["time"][i]).strftime("%A, %B %d")
                output += f"\n{date}:\n"
                output += f"  High: {daily['temperature_2m_max'][i]}°C\n"
                output += f"  Low: {daily['temperature_2m_min'][i]}°C\n"
                output += f"  Precipitation: {daily['precipitation_sum'][i]} mm\n"
                output += f"  Max Wind: {daily['wind_speed_10m_max'][i]} km/h\n"
                output += f"  Conditions: {self._get_weather_description(daily['weather_code'][i])}\n"
            
            return output
            
        except requests.exceptions.RequestException as e:
            return f"Error fetching weather data: {str(e)}"
        except Exception as e:
            return f"Unexpected error: {str(e)}"
    
    def _get_weather_description(self, code: int) -> str:
        """Convert WMO weather code to description."""
        weather_codes = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Foggy",
            48: "Depositing rime fog",
            51: "Light drizzle",
            53: "Moderate drizzle",
            55: "Dense drizzle",
            61: "Slight rain",
            63: "Moderate rain",
            65: "Heavy rain",
            71: "Slight snow",
            73: "Moderate snow",
            75: "Heavy snow",
            77: "Snow grains",
            80: "Slight rain showers",
            81: "Moderate rain showers",
            82: "Violent rain showers",
            85: "Slight snow showers",
            86: "Heavy snow showers",
            95: "Thunderstorm",
            96: "Thunderstorm with slight hail",
            99: "Thunderstorm with heavy hail"
        }
        return weather_codes.get(code, f"Unknown (code: {code})")