#include <Arduino.h>
#include <Adafruit_Neopixel.h>

#define PIN  7
#define SIZE  12
#define FPS 15

const int pixelCount = SIZE * SIZE;

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(SIZE*SIZE, PIN, NEO_GRB + NEO_KHZ400);


byte input[pixelCount][3];


void setup() {
  pixels.begin();
  pixels.setBrightness(128);
  Serial.begin(230400);
  Serial.setTimeout(5000);
  pixels.clear();
  pixels.show();
}

// put function definitions here:


void drawPixels(byte in[pixelCount][3]){
  pixels.clear();
  for(int i = 0; i < pixelCount; i ++){
    uint32_t color = pixels.Color(in[i][0], in[i][1], in[i][2]);
    //uint32_t color = pixels.Color(0, 255, 255);
    pixels.setPixelColor(i, color);
  }
  pixels.show();
}

#include <Arduino.h>
#include <Adafruit_Neopixel.h>

#define PIN  7
#define SIZE  12
#define FPS 15

const int pixelCount = SIZE * SIZE;

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(SIZE*SIZE, PIN, NEO_GRB + NEO_KHZ400);

byte cmd_buffer[64];
byte input[pixelCount][3];


void setup() {
  pixels.begin();
  pixels.setBrightness(128);
  Serial.begin(230400);
  Serial.setTimeout(5000);
  pixels.clear();
  pixels.show();
}

// put function definitions here:


void drawPixels(byte in[pixelCount][3]){
  pixels.clear();
  for(int i = 0; i < pixelCount; i ++){
    uint32_t color = pixels.Color(in[i][0], in[i][1], in[i][2]);
    //uint32_t color = pixels.Color(0, 255, 255);
    pixels.setPixelColor(i, color);
  }
  pixels.show();
}

void readSerial(){
  /*
    ACCEPTABLE COMMANDS:
    cm - clear matrix; no args
    EXAMPLE: cm:\0
    -------------------
    sp - set pixel; args: x, y, r, g, b
    EXAMPLE: sp:0,0,255,0,0:\0
  */
  char cmd_id[2] = {0};
  char cmd_args[61] = {0};

  Serial.readBytesUntil('\0', cmd_buffer, 4);
  memcpy(cmd_id, cmd_buffer, 2);
  
  switch cmd_id {
    case "cm":
      pixels.clear();
      pixels.show();
      break;

    case "sp":
      strcpy(cmd_args, cmd_buffer + 3);
      int x = atoi(strtok(cmd_args, ","));
      int y = atoi(strtok(NULL, ","));
      int r = atoi(strtok(NULL, ","));
      int g = atoi(strtok(NULL, ","));
      int b = atoi(strtok(NULL, ","));
      uint32_t color = pixels.Color(r, g, b);
      pixels.setPixelColor(x + y * SIZE, color);
      pixels.show();
      break;
    default:
      break;
  } 

}

void loop() {
  while(Serial.available() != 0){
    delay(50);
  }   
  readSerial();
  drawPixels(input);

}

void loop() {
  while(Serial.isAvailable() != 0){
    delay(50)
  }   
  readSerial();
  drawPixels(input);

}