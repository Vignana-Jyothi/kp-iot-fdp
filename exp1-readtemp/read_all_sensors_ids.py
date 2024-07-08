import time
from w1thermsensor import W1ThermSensor

# Find all available sensors
sensors = W1ThermSensor.get_available_sensors()

while True:
    try:
        # Iterate through all sensors and print their temperatures
        for sensor in sensors:
            temperature = sensor.get_temperature()
            print(f"Sensor {sensor.id} Temperature: {temperature:.2f} °C")
    except Exception as e:
        print(f"Error: {e}")
    
    # Wait for a second before reading again
    time.sleep(1)
