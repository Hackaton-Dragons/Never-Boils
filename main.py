# Modulates the temperature of the pot
import photo_finder.py as findMyPhoto
import arduino.py as getTemp
import face.py as face
import time

def checkEyeContact(eyeContact):
    if eyeContact == True:
        return True
    else:
        return False

def setRelay(modTemp,temp):
    #Output the value to the relay mod
    if temp < 90:
        getTemp.turn_relay_on()
    elif temp < 90 and modTemp == True:
        getTemp.turn_relay_off()
    elif temp > 90 and temp < 100 and modTemp == False:
        getTemp.turn_relay_on()
    elif temp > 90 and temp < 100 and modTemp == True:
        getTemp.turn_relay_off()
    elif temp > 100 and temp < 110 and modTemp == True:
        getTemp.turn_relay_off()
    elif temp > 100 and temp < 110 and modTemp == False:
        getTemp.turn_relay_on()
    elif temp > 110:
        getTemp.turn_relay_off()

def main():
    run = True
    while run:
        time.sleep(15)
        image = findMyPhoto.main()
        checkHere = FaceChecker(image)
        eyeContact = checkHere.check()
        modTemp = checkEyeContact(eyeContact)
        temp = readSerial.getTemp()
        setRelay(modTemp,temp)
        
main(True)
