# Import the necessary modules
from araweather import weather
from arapower import power

# Function to get and print the current weather data
def fetch_and_print_weather_data(locations):
    weather_data = weather.get_current_weather(locations)
    print("Current Weather Data:", weather_data)

# Function to get and print the current aggregate power data
def fetch_and_print_power_data(locations):
    power_data = power.get_current_aggregate_power(locations)
    print("Current Aggregate Power Data:", power_data)

# Main function to execute our API calls
def main():
    locations = ['WilsonHall']  # Locations can be modified as needed
    fetch_and_print_weather_data(locations)
    fetch_and_print_power_data(locations)

# Execute the main function
if __name__ == "__main__":
    main()
