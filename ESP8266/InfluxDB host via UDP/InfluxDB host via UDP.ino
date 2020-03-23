#include <SPI.h>
#include <WiFi.h>
#include <WiFiUDP.h>

char ssid[] = "your network name";     //  your network SSID (name) 
char pass[] = "network password";    // your network password
int status = WL_IDLE_STATUS;     // the Wifi radio's status

// the IP address of your InfluxDB host
byte host[] = {10, 0, 1, 11};

// the port that the InfluxDB UDP plugin is listening on
int port = 8888;

WiFiUDP udp;

void setup() {
  // initialize serial port
  Serial.begin(9600);

  // attempt to connect using WPA2 encryption
  Serial.println("Attempting to connect to WPA network...");
  status = WiFi.begin(ssid, pass);

  // if unable to connect, halt
  if ( status != WL_CONNECTED) { 
    Serial.println("Couldn't get a WiFi connection");
    while(true);
  } 
  // if the conneciton succeeded, print network info
  else {
    Serial.println("Connected to network");
    // print your WiFi shield's IP address:
    IPAddress ip = WiFi.localIP();
    Serial.print("IP Address: ");
    Serial.println(ip);

    // print the received signal strength:
    long rssi = WiFi.RSSI();
    Serial.print("signal strength (RSSI):");
    Serial.print(rssi);
    Serial.println(" dBm");
  }
}

float getTemperature() {
  // get the reading from the temperature sensor
  int reading = analogRead(0);
 
  // convert that reading to voltage
  float voltage = reading * 5.0;
  voltage /= 1024.0; 
 
  // convert the voltage to temperature in Celsius (10mV per degree + 500mV offset)
  float temperatureC = (voltage - 0.5) * 100 ;  
  
  // now convert to Fahrenheit
  float temperatureF = (temperatureC * 9.0 / 5.0) + 32.0;

  return temperatureF;
}

void loop() {
  String line, temperature;

  // wait 1 second
  delay(1000);
  
  // get the current temperature from the sensor, to 2 decimal places
  temperature = String(getTemperature(), 2);

  // concatenate the temperature into the line protocol
  line = String("temperature value=" + temperature);
  Serial.println(line);
  
  // send the packet
  Serial.println("Sending UDP packet...");
  udp.beginPacket(host, port);
  udp.print(line);
  udp.endPacket();
}