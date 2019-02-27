#include <TrinketUSB.h>

long long lastTime = 0; 

#define LED 1

void setup()
{
  // start USB stuff
  TrinketKeyboard.begin();
  lastTime = millis();
  pinMode(LED, OUTPUT);
}

void loop()
{
  TrinketKeyboard.poll();

  long long now = millis();
  if (now - lastTime > 2000) { 
    TrinketKeyboard.print("trinket");
    lastTime = now;
    digitalWrite(LED, HIGH); 
  }
  else if (now - lastTime > 300) { 
    digitalWrite(LED, LOW); 
  }
}
