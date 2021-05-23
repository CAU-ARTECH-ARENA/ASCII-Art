import processing.video.*;
import java.awt.*;

String string;
PFont font;
PImage img;

Capture cam;
Rectangle[] faces;

void setup() {
  colorMode(RGB);
  size(640, 480);
  background(0);
  string = "@";
  //font = loadFont("Arial-Black-48.vlw");
  cam = new Capture(this, 640, 480);
  
  cam.start();
}

int ack=1;
int index;
int size=1;

void draw() {
  background(0);
  //image(cam, 0, 0);
  ack= (ack > 200) ? 1 : ack+1;
  index=0; 
  color c;
  for (int i=0; i<=width; i+=width/55)
  {
    for (int j=0; j<=height+40; j+=height/40)
    {
      c = cam.get(i, j);
      float d = map(brightness(c), 0, 255, 60, 0);
      textSize(14-size);
      fill(c);
      index++;
      //println(c);
      float temp = red(c) + green(c) + blue(c);
      if(temp/3 > 120){ fill(255);
      text(string.charAt((index)%string.length()), i, j);}
    }
  }
}

void captureEvent(Capture c) {
  c.read();
}

void keyPressed()
{
  if(key=='q'){ size+=1; }
  if(key=='w'){ size-=1; }
}
    
  
