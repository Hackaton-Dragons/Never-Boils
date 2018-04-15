import time

import camera
import arduino 
import face

DELAY_SEGMENTS = 3
DELAY = 3

IMAGE_FILE = "images/photo.bmp"
OLD_IMAGE_FILE = "images/old.bmp"

HOLDING_TEMP = 90
BOILING_TEMP = 100
MAX_BOILING_TEMP = 102

def control_loop(face_checker, cam, delay):
    cam.get_image()

    temp = arduino.get_temp()

    print("temp={}".format(temp))

    if temp < HOLDING_TEMP:
        arduino.turn_relay_on()
    else:
        eye_contact = face_checker.check()

        print("eye contact={}".format(eye_contact))

        if eye_contact:
            arduino.turn_relay_off()
        else:
            if temp > MAX_BOILING_TEMP:
                arduino.turn_relay_off()
            else:
                arduino.turn_relay_on()

    delay_part = DELAY / DELAY_SEGMENTS
    accum_delay = 0

    for i in range(DELAY_SEGMENTS):
        accum_delay += delay_part

        print("sleeping for {} more seconds".format(int(DELAY - accum_delay)))

        time.sleep(delay_part)

def main():
    face_checker = face.FaceChecker(IMAGE_FILE, OLD_IMAGE_FILE, request_delay=DELAY)
    cam = camera.WebCam(IMAGE_FILE)

    try:
        while True:
            control_loop(face_checker, cam, DELAY)
    except KeyboardInterrupt:
        print("stopping")

if __name__ == '__main__':
    main()
