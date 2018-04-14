import serial       #requires python-serial to be installed on system


arduino_location = '/dev/ttyACM0'
arduino_port = 9600
arduino = serial.Serial(arduino_location, arduino_port)

def get_temp():
    print(arduino.read(5).decode())