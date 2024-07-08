import time
from w1thermsensor import W1ThermSensor, Sensor


# Initialize the sensors by their IDs
# Replace '28-xxxxxxxxxxxx' with your actual sensor IDs
sensor_1 = W1ThermSensor(sensor_type=Sensor.DS18B20, sensor_id='3c01a816ebb5')
sensor_2 = W1ThermSensor(sensor_type=Sensor.DS18B20, sensor_id='3c01a8168ab9')

# 28-3c01a816805f  28-3c01a816dda7  w1_bus_master1  w1_bus_master3
# 28-3c01a8168ab9  28-3c01a816ebb5  w1_bus_master2  w1_bus_master4

while True:
    # Read temperature in Celsius from both sensors
    temperature_1 = sensor_1.get_temperature()
    temperature_2 = sensor_2.get_temperature()
    
    
    # Print the temperatures
    print(f"Sensor 1 Temperature: {temperature_1:.2f} °C")
    print(f"Sensor 2 Temperature: {temperature_2:.2f} °C")

    # Wait for a second before reading again
    time.sleep(1)
