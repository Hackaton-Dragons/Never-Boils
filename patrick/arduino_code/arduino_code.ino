/********************************************************************/
// First we include the libraries
// tutorial with links at https://create.arduino.cc/projecthub/TheGadgetBoy/ds18b20-digital-temperature-sensor-and-arduino-9cc806
#include <OneWire.h> 
#include <DallasTemperature.h>
/********************************************************************/
// Data wire is plugged into pin 2 on the Arduino 
#define ONE_WIRE_BUS 2 
/********************************************************************/
// Setup a oneWire instance to communicate with any OneWire devices  
// (not just Maxim/Dallas temperature ICs) 
OneWire oneWire(ONE_WIRE_BUS); 
/********************************************************************/
// Pass our oneWire reference to Dallas Temperature. 
DallasTemperature sensors(&oneWire);
/********************************************************************/ 
void setup(void) 
{ 
 // start serial port 
 Serial.begin(9600); 
 //Serial.println("Dallas Temperature IC Control Library Demo"); 
 // Start up the library 
 sensors.begin(); 
 pinMode(LED_BUILTIN, OUTPUT);  //pin 13 on the uno. used for the relay
} 
void loop(void) 
{ 
 // call sensors.requestTemperatures() to issue a global temperature 
 // request to all devices on the bus 
/********************************************************************/
 sensors.requestTemperatures(); // Send the command to get temperature readings  
/********************************************************************/
 Serial.print(sensors.getTempCByIndex(0)); // Why "byIndex"?  
   // You can have more than one DS18B20 on the same bus.  
   // 0 refers to the first IC on the wire

 if(Serial.available() > 0)
 {
    char incoming = Serial.read();   //may need to be chnaged to char
    switch(incoming)
    {
      case '0':
        digitalWrite(LED_BUILTIN, LOW);   //again, the relay
        break;
      case '1':
        digitalWrite(LED_BUILTIN, HIGH);
      }
  }
   
   delay(1000); 
} 
