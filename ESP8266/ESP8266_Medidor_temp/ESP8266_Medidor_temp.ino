/**
 * Basic Write Example code for InfluxDBClient library for Arduino
 * Data can be immediately seen in a InfluxDB UI: wifi_status measurement
 * Enter WiFi and InfluxDB parameters below
 *
 * Measures signal level of the actually connected WiFi network
 * This example supports only InfluxDB running from unsecure (http://...)
 * For secure (https://...) or Influx Cloud 2 use SecureWrite example
 **/

#if defined(ESP32)
#include <WiFiMulti.h>
WiFiMulti wifiMulti;
#define DEVICE "ESP32"
#elif defined(ESP8266)
#include <ESP8266WiFiMulti.h>
ESP8266WiFiMulti wifiMulti;
#define DEVICE "ESP8266"
#endif
#include <InfluxDbClient.h>
#include <DHT.h>

// WiFi AP SSID
#define WIFI_SSID "WifiSiTo"
// WiFi password
#define WIFI_PASSWORD "2210198531011990"
// InfluxDB  server url. Don't use localhost, always server name or ip address.
// For InfluxDB 2 e.g. http://192.168.1.48:9999 (Use: InfluxDB UI -> Load Data -> Client Libraries), 
// For InfluxDB 1 e.g. http://192.168.1.48:8086
#define INFLUXDB_URL "http://192.168.1.212:8086"
// InfluxDB 2 server or cloud API authentication token (Use: InfluxDB UI -> Load Data -> Tokens -> <select token>)
//#define INFLUXDB_TOKEN "toked-id"
// InfluxDB 2 organization id (Use: InfluxDB UI -> Settings -> Profile -> <name under tile> )
//#define INFLUXDB_ORG "org"
// InfluxDB 2 bucket name (Use: InfluxDB UI -> Load Data -> Buckets)
//#define INFLUXDB_BUCKET "bucket"
// InfluxDB v1 database name 
#define INFLUXDB_DB_NAME "telegraf"

//Usuario Influx
#define INFLUXDB_USER "admin"

//Password Influx
#define INFLUXDB_PASSWORD "emperador"

// InfluxDB client instance
//InfluxDBClient client(INFLUXDB_URL, INFLUXDB_ORG, INFLUXDB_BUCKET, INFLUXDB_TOKEN);
// InfluxDB client instance for InfluxDB 1
InfluxDBClient client(INFLUXDB_URL, INFLUXDB_DB_NAME);

#define DHTPIN 2     // Vamos a probar con GPIO2

#define DHTTYPE    DHT11     // DHT 11

DHT dht(DHTPIN, DHTTYPE);

// Data point
Point sensor1("RSSI");
Point sensor2("DHT11_Temperatura");
Point sensor3("DHT11_Humedad");

void setup() {
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
  Serial.println();

  // Set InfluxDB 1 authentication params
  client.setConnectionParamsV1(INFLUXDB_URL, INFLUXDB_DB_NAME, INFLUXDB_USER, INFLUXDB_PASSWORD);

  // Add constant tags - only once
  sensor1.addTag("device", DEVICE);
  sensor2.addTag("DHT11_temp", DEVICE);
  sensor3.addTag("DHT11_hum", DEVICE);

  // Check server connection
  if (client.validateConnection()) {
    Serial.print("Connected to InfluxDB: ");
    Serial.println(client.getServerUrl());
  } else {
    Serial.print("InfluxDB connection failed: ");
    Serial.println(client.getLastErrorMessage());
  }
}
  
void loop() {

  Serial.print("Temperatura: ");
  Serial.print(dht.readTemperature());
  Serial.println(" ºC");

  Serial.print("Humedad: ");
  Serial.print(dht.readHumidity());
  Serial.println(" %"); 

  // Store measured value into point
  sensor1.clearFields();
  sensor2.clearFields();
  sensor3.clearFields();
  // Report RSSI of currently connected network
  sensor1.addField("rssi", WiFi.RSSI());
  sensor2.addField("Temperatura", dht.readTemperature());
  sensor3.addField("Humedad", dht.readHumidity());

  // Print what are we exactly writing
  Serial.print("Writing: ");
  Serial.println(sensor1.toLineProtocol());
  Serial.println(sensor2.toLineProtocol());
  Serial.println(sensor3.toLineProtocol());
  Serial.println("Writing finished");
  // If no Wifi signal, try to reconnect it
  if ((WiFi.RSSI() == 0) && (wifiMulti.run() != WL_CONNECTED))
    Serial.println("Wifi connection lost");
  // Write point
  if (!client.writePoint(sensor1)) {
    Serial.print("InfluxDB write failed: ");
    Serial.println(client.getLastErrorMessage());
  }

  //Wait 10s
  Serial.println("Wait 10s");
  delay(10000);
}
