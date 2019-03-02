
#include <TrinketUSB.h>

#define LED 1
#define BASE2n222 2

void setup()
{
  // start USB stuff
  usbBegin();
  pinMode(LED, OUTPUT);
  
  pinMode(BASE2n222, OUTPUT); 
  digitalWrite(BASE2n222, LOW);

  for (int i = 0; i < 2; i++) { 
    digitalWrite(LED, HIGH);
    delay(300);
    digitalWrite(LED, LOW);
    delay(300); 
  }
}

void loop()
{
  usbPollWrapper();
  digitalWrite(LED, usbLEDState);
  digitalWrite(BASE2n222, usbLEDState);
}
