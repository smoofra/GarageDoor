
#include <TrinketUSB.h>

#define LED 1

void setup()
{
  // start USB stuff
  usbBegin();
  pinMode(LED, OUTPUT);

  for (int i = 0; i < 3; i++) { 
    digitalWrite(LED, HIGH);
    delay(300);
    digitalWrite(LED, LOW);
    delay(300); 
  }
}

void loop()
{
  usbPollWrapper();
}
