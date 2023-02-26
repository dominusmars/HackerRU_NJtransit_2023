"""
int relay1 = 2;
int relay2 = 3;

const int triggerType = LOW;// your relay type

int relayOFF, relayON;// relay ON and OFF values for LOW and HIGH Trigger relays



void setup() {

    pinMode(relay1, OUTPUT);// set pin as output for relay 1
    pinMode(relay2, OUTPUT);// set pin as output for relay 2


    if(triggerType ==LOW){
      relayON = LOW;
      relayOFF = HIGH;
      digitalWrite(relay1, relayOFF);//keep both relay OFF so motor is stopped
      digitalWrite(relay2, relayOFF);//keep both relay OFF so motor is stopped
    }else{
      relayON = HIGH;
      relayOFF = LOW; 
      digitalWrite(relay1, relayOFF);//keep both relay OFF so motor is stopped
      digitalWrite(relay2, relayOFF);//keep both relay OFF so motor is stopped
    }
 
  
  Serial.begin(9600);// initialize serial monitor with 9600 baud
  Serial.println("Robojax Motor Direction of Rotation");
  Serial.println("Using 2 Relays");  
  delay(2000);
}

void loop() {

 // Rotate in CCW direction
  motorCCW(); 
  delay(3000);// wait for 3 seconds

  motorStop();
  delay(2000);
  
 // Rotate in CW direction
  motorCW();
  delay(3000);// wait for 3 seconds

 motorStop();
 delay(2000);
  
 Serial.println("===============");
          
}// loop end

/*
 * motorCCW() 
 * controls the relay so the motor rotates in CCW
 */
void motorCCW()
{
  digitalWrite(relay1, relayON);// turn relay 1 ON
  digitalWrite(relay2, relayOFF);// turn relay 2 OFF  
  Serial.println("Rotating in CCW");    
}// motorCCW()


/*
 * motorCW() 
 * controls the relay so the motor rotates in CW
 */
void motorCW()
{
  digitalWrite(relay1, relayOFF);// turn relay 1 OFF
  digitalWrite(relay2, relayON);// turn relay 2 ON 
  Serial.println("Rotating in CW");  
}//motorCW()


/*
 * motorStop()
 * controls the relay so the motor is stopped
 */
void motorStop()
{
  digitalWrite(relay1, relayOFF);// turn relay 1 OFF
  digitalWrite(relay2, relayOFF);// turn relay 2 OFf 
  Serial.println("Stopped");    
} 
"""

import RPi.GPIO as GPIO
import time

class Motor():
    
    def __init__(self):
        
        GPIO.setmode(GPIO.BCM)

        self.a = 16    #motor group A - up
        self.b = 20    #motor group A - down
        self.c = 18    #motor group B - up
        self.d = 19    #motor group B - down

        GPIO.setup(16, GPIO.OUT)
        GPIO.setup(20, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(19, GPIO.OUT)
    
    def motorupA(self):
        """
        digitalWrite(relay1, relayON);// turn relay 1 ON
        digitalWrite(relay2, relayOFF);
        """
        GPIO.output(self.a, GPIO.LOW)
        GPIO.output(self.b, GPIO.HIGH)
        
        
    def motordownA(self):
        
        """
        digitalWrite(relay1, relayOFF);// turn relay 1 ON
        digitalWrite(relay2, relayON);// turn relay 2 OFF
        """
        GPIO.output(self.a, GPIO.HIGH)
        GPIO.output(self.b, GPIO.LOW)
        
    def motorstopA(self):
        
        GPIO.output(self.a, GPIO.LOW)
        GPIO.output(self.b, GPIO.LOW)
        
    def motorupB(self):
        """
        digitalWrite(relay1, relayON);// turn relay 1 ON
        digitalWrite(relay2, relayOFF);
        """
        GPIO.output(self.c, GPIO.LOW)
        GPIO.output(self.d, GPIO.HIGH)
        
        
    def motordownB(self):
        
        """
        digitalWrite(relay1, relayOFF);// turn relay 1 ON
        digitalWrite(relay2, relayON);// turn relay 2 OFF
        """
        GPIO.output(self.c, GPIO.HIGH)
        GPIO.output(self.d, GPIO.LOW)
        
    def motorstopB(self):
        
        GPIO.output(self.c, GPIO.LOW)
        GPIO.output(self.d, GPIO.LOW)
        
t = Motor()

count=0
while(count < 3):
    count+=1
    
    t.motorupA()
    time.sleep(2)
    
    t.motorstopA()
    time.sleep(0.5)
    
    t.motordownA()
    time.sleep(2)
    
    t.motorstopA()
    time.sleep(0.5)
    
    

t.motorstopA()
        


"""
while (True):
    GPIO.output(re, GPIO.LOW)
    time.sleep(2)
    GPIO.output(re, GPIO.HIGH)
    time.sleep(2)
    
"""
