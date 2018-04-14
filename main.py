# Modulates the temperature of the pot
# import eye tracker

import photo_finder.py as findMyPhoto
import arduino.py as getTemp
import face.py as face
import time

def checkEyeContact(eyeContact):
    if eyeContact == True:
        return True
    else:
        return False

def setRelay(val):
    #Output the value to the relay mod
    pass

def main():
    run = True
    while run:
        time.sleep(15)
        image = findMyPhoto.main()
        checkHere = FaceChecker(image)
        eyeContact = checkHere.check()
        print(eyeContact)
        modTemp = checkEyeContact(eyeContact)
        temp = readSerial.getTemp()
        val = bool
        if modTemp == True:
            val = True
            setRelay(val)
        else:
            val = False
            setRelay(val)

main(True)
