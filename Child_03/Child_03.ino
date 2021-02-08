/*
  Arduino Wireless Network - Multiple NRF24L01 Tutorial
 == Example 01 - Servo Control / Node 00 - Potentiometer ==
  by Dejan, www.HowToMechatronics.com
  Libraries:
  nRF24/RF24, https://github.com/nRF24/RF24
  nRF24/RF24Network, https://github.com/nRF24/RF24Network
*/
#include <RF24.h>
#include <RF24Network.h>
#include <SPI.h>

#define DELAY_MS 10

unsigned long Device_id = 333;

RF24 radio(10, 9);               // nRF24L01 (CE,CSN)
RF24Network network(radio);      // Include the radio in the network
const uint16_t base_node = 00;   // Address of this node in Octal format ( 04,031, etc)
const uint16_t this_node = 03;      

void setup() {
  SPI.begin();
  radio.begin();
  network.begin(90, this_node);  //(channel, node address)
  pinMode(7,OUTPUT);
  digitalWrite(7,LOW);
}

void loop() {
  network.update();
  RF24NetworkHeader header(base_node);     // (Address where the data is going)
  bool ok = network.write(header, &Device_id, sizeof(Device_id)); // Send the data
  digitalWrite(7,HIGH);
  delay(DELAY_MS);
  digitalWrite(7,LOW);
  delay(DELAY_MS);
}
