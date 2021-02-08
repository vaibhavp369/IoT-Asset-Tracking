/*
on ESP NODE MCU
*/
#include <RF24.h>
#include <RF24Network.h>
#include <SPI.h>
#include <ESP8266WiFi.h>
#include <PubSubClient.h>

char raw_asset_data[5] = {'$','0','0','0'};

char incoming_data_flag[4] = {'0','0','0','0'};

RF24 radio(2, 4);               // nRF24L01 (CE,CSN)
RF24Network network(radio);      // Include the radio in the network
const uint16_t this_node = 00;   // Address of our node in Octal format ( 04,031, etc)

const long interval = 500; 

const char* ssid = "HR";                           //!!!!!!!!!!!!!!!!!!!!!
const char* password = "123123123";                //!!!!!!!!!!!!!!!!!!!!!
const char* mqtt_server = "broker.hivemq.com";     // 192.168.43.78

WiFiClient Asset_node;
PubSubClient client(Asset_node);


unsigned long previousMillis = 0;

void setup() 
{
    SPI.begin();
    radio.begin();
    network.begin(90, this_node); //(channel, node address)
    Serial.begin(9600);
    delay(10);
    WiFi.mode(WIFI_STA);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) 
      {
        delay(500);
      }
   client.setServer(mqtt_server, 1883);
   client.setCallback(callback);
   pinMode(D0,OUTPUT);
   pinMode(D0,LOW);
}


void loop() 
{

   if (!client.connected()) 
   {
     reconnect();
   }
  unsigned long currentMillis = millis();
  client.loop();
  network.update();
  while ( network.available() ) // Is there any incoming data?
  {     
      RF24NetworkHeader header;
      unsigned long incomingData;
      for(int asset_no =1; asset_no <=3 ;asset_no++)
        {
            network.read(header, &incomingData, sizeof(incomingData)); // Read the incoming data
            incoming_data_flag[header.from_node] = '1';
        }  

       for(int asset_no =1; asset_no <=3;asset_no++)
        {
            if(incoming_data_flag[asset_no] == '1')
                raw_asset_data[asset_no] = '1';
             else
                raw_asset_data[asset_no] = '0';
        }

        
  }
        
 
  if (currentMillis - previousMillis >= interval)         // Reset the flag every 2 seconds
    {
        client.publish("Asset_tracking",raw_asset_data);
        previousMillis = currentMillis;
        incoming_data_flag[0] = '0';raw_asset_data[0] = '$';
        incoming_data_flag[1] = '0';raw_asset_data[1] = '0';
        incoming_data_flag[2] = '0';raw_asset_data[2] = '0';
        incoming_data_flag[3] = '0';raw_asset_data[3] = '0';
        if(digitalRead(D0))
          digitalWrite(D0,LOW);
        else
          digitalWrite(D0,HIGH);
    }
    
}

void callback(char* topic, byte* payload, unsigned int length) // To Read any incoming data from MQTT
{
 
   delay(100);
   for (int i=0;i<length;i++) 
      {
        char receivedChar = (char)payload[i];
        Serial.write(receivedChar);
      }
}


int reconnect()          // Reconnect to broker if get disconnected !!!
{
   while (!client.connected()) 
     {
    
     if (client.connect("Asset_node")) 
         {
           return 0;
         } 
     else 
        {
        delay(3000);
        }
     }
}
