#if defined(ESP32)
#include <WiFiMulti.h>
WiFiMulti wifiMulti;
#define DEVICE "ESP32"
#elif defined(ESP8266)
#include <ESP8266WiFiMulti.h>
ESP8266WiFiMulti wifiMulti;
#define DEVICE "ESP8266"
#endif

#include <SPI.h>
#include <WiFiUDP.h>
#include <DHT.h>

// WiFi AP SSID
#define WIFI_SSID "WifiSiTo"
// WiFi password
#define WIFI_PASSWORD "2210198531011990"

// the IP address of your InfluxDB host
byte host[] = {192, 168, 1, 212};

// the port that the InfluxDB UDP plugin is listening on
int port = 8086;

WiFiUDP udp;

#define DHTPIN 2     // Vamos a probar con GPIO2
#define DHTTYPE    DHT11     // DHT 1

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  // initialize serial port
  Serial.begin(115200);
  dht.begin();

// Connect WiFi
  Serial.println("Connecting to WiFi");
  WiFi.mode(WIFI_STA);
  wifiMulti.addAP(WIFI_SSID, WIFI_PASSWORD);
  while (wifiMulti.run() != WL_CONNECTED) {
    Serial.print(".");
    delay(100);
  }

  if (wifiMulti.run() == WL_CONNECTED)
  {
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

  Serial.println();
}

void loop() {
  String line, temperature;

  // wait 1 second
  delay(1000);
  
  // get the current temperature from the sensor, to 2 decimal places
  temperature = String(dht.readTemperature(), 2);

  Serial.print("Temp = ");
  Serial.println(temperature);

  // concatenate the temperature into the line protocol
  line = String("temperature value=" + temperature);
  Serial.println(line);
  
  // send the packet
  Serial.println("Sending UDP packet...");
  udp.beginPacket(host, port);
  udp.print(line);
  udp.endPacket();
}
