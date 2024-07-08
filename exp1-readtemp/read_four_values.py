import time
from w1thermsensor import W1ThermSensor

# Initialize the sensors by their IDs
sensor_1 = W1ThermSensor(sensor_id='3c01a816805f')
sensor_2 = W1ThermSensor(sensor_id='3c01a8168ab9')
sensor_3 = W1ThermSensor(sensor_id='3c01a816dda7')
sensor_4 = W1ThermSensor(sensor_id='3c01a816ebb5')

while True:
    try:
        # Read temperature in Celsius from all sensors
        temperature_1 = sensor_1.get_temperature()
        temperature_2 = sensor_2.get_temperature()
        temperature_3 = sensor_3.get_temperature()
        temperature_4 = sensor_4.get_temperature()
        
        # Print the temperatures
        print(f"Sensor 1 Temperature: {temperature_1:.2f} °C")
        print(f"Sensor 2 Temperature: {temperature_2:.2f} °C")
        print(f"Sensor 3 Temperature: {temperature_3:.2f} °C")
        print(f"Sensor 4 Temperature: {temperature_4:.2f} °C")
    except Exception as e:
        print(f"Error: {e}")
    
    # Wait for a second before reading again
    time.sleep(1)
