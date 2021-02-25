
""" 
dht11.py 

Temperature/Humidity monitor using Raspberry Pi and DHT22. 
Data is displayed at thingspeak.com
Original author: Austinstevesk
""" 

import sys 
import RPi.GPIO as GPIO 
from time import sleep 
import Adafruit_DHT 
import urllib3 

myAPI = "<your API code here>" 

def getSensorData(): 
   RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 17) #17 refers to GPIO 17, or pin 6 on the RPi
   return (str(RH), str(T)) 

def main(): 
   print('starting...') 
   baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI 

   while True: 
       try: 
           RH, T = getSensorData() 
           f = urllib3.urlopen(baseURL + 
                               "&field1=%s&field2=%s" % (RH, T)) #Send/Update the data
           print(f.read()) 
           f.close() 
           sleep(300) #uploads DHT11 sensor values every 5 minutes 
       except: 
           print('exiting.') 
           break 

# call main:
if __name__ == '__main__': 
   main() 

