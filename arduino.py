import serial       #requires python-serial to be installed on system
import time

arduino_location = '/dev/ttyACM0'
arduino_port = 9600
arduino = serial.Serial(arduino_location, arduino_port)

def get_temp():
    raw = arduino.readline()
    return float(raw.decode())

def turn_relay_on():
    arduino.write('1'.encode())
    print("relay on")

def turn_relay_off():
    arduino.write('0'.encode())
    print("relay off")

# Run test code if invoked and not included
if __name__ == '__main__':
    print(get_temp())
