import serial       #requires python-serial to be installed on system
import time

arduino_location = '/dev/ttyACM0'
arduino_port = 9600
arduino = serial.Serial(arduino_location, arduino_port)

def get_temp():
    return arduino.read(5).decode()

def turn_relay_on():
    arduino.write('1'.encode())

def turn_relay_off():
    arduino.write('0'.encode())

# Run test code if invoked and not included
if __name__ == '__main__':
    for i in range(200):
        turn_relay_on()
        time.sleep(5)
        turn_relay_off()
        get_temp()
