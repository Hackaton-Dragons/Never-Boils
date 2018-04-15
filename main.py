import time

import camera
import arduino 
import face

DELAY = 15
IMAGE_FILE = "images/photo.png"

def control_loop(face_checker, camera, delay):
    camera.get_image()
    eye_contact = face_cheker.check()

    print("eye contact={}".format(eye_contact)

    temp = readSerial.get_temp()

    if eye_contact:
        arduino.turn_relay_off()
    else:
        arduino.turn_relay_on()

    time.sleep(DELAY)

def main():
    face_checker = FaceChecker(IMAGE_FILE, request_delay=DELAY)
    camera = camera.Camera(IMAGE_FILE)

    try:
        while True:
            control_loop(face_checker, camera, delay)
    except KeyboardInterrupt:
        print("stopping")

    camera.stop()

if __name__ == '__main__':
    main()
