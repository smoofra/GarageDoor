#include <TrinketUSB.h>

#define LED 1

void setup()
{
  // start USB stuff
  usbBegin();
  pinMode(LED, OUTPUT);
}

void loop()
{
  usbPollWrapper();
}
