#include <Arduino.h>
#include <Adafruit_Neopixel.h>

#define PIN  7
#define SIZE  12
#define FPS 15

const int pixelCount = SIZE * SIZE;

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(SIZE*SIZE, PIN, NEO_GRB + NEO_KHZ400);


byte input[pixelCount][3];
int brightness = 100;


void setup() {
  pixels.begin();
  pixels.setBrightness(brightness);
  Serial.begin(230400);
  Serial.setTimeout(5000);
  pixels.clear();
  pixels.show();

  Serial.println("init");
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
  for(int i = 0; i< pixelCount; i++){
    Serial.readBytes(input[i], 3);

    //Serial.println("");
    Serial.print(String(input[i][0]) + ",");
    Serial.print(String(input[i][1]) +",");
    Serial.println(String(input[i][2])+ "," );
  }
}

void adjustBrightness(){
  int in = analogRead(A3);
  int newBright = in / 4;
  if (newBright != brightness){
    brightness = newBright;
    pixels.setBrightness(brightness);
    pixels.show();
  }
}

void loop(){
  if (Serial.available() > 0){
    readSerial();
    drawPixels(input);
  }
  //adjustBrightness();
  }


