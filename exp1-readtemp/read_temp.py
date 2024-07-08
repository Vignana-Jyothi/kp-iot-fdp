import time
from w1thermsensor import W1ThermSensor

# Initialize the sensor
sensor = W1ThermSensor()

while True:
    # Read temperature in Celsius
    temperature = sensor.get_temperature()
    
    # Print the temperature
    print(f"Temperature: {temperature:.2f} °C")
    
    # Wait for a second before reading again
    time.sleep(1)
