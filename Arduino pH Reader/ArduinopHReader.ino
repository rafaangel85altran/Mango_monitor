// pHRead.ino

#include <LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

// Constants:-
const byte pHpin = A0;// Connect the sensor's Po output to analogue pin 0.

// Variables:-
float Po;

void setup()
{
Serial.begin(9600);
lcd.begin(16, 2);             // set up the LCD's number of columns and rows:
lcd.print("hello, world!");   // Print a message to the LCD.
}

void loop()
{
  Po = (1023 - analogRead(pHpin)) / 73.07; // Read and reverse the analogue input value from the pH sensor then scale 0-14.
  Serial.println(Po, 2);// Print the result in the serial monitor.
  lcd.setCursor(0, 0);
  lcd.print("PH = ");
  lcd.setCursor(5, 0);
  lcd.print(Po,2);
  lcd.setCursor(9, 0);
  lcd.print("       ");
  lcd.setCursor(0, 1);
  lcd.print("                ");
  
  delay(1000);// Take 1 reading per second.
  
}
