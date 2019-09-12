#include <DallasTemperature.h>
#include <OneWire.h>

float last_temp[5]={0,0,0,0,0};
float current_temp[5]={0,0,0,0,0};

int done[5]={0,0,0,0,0};//if near 0 C for over 2 min, considered done
int cnt=0;

int wait=5000;

unsigned long t_time=0; //in seconds

unsigned int offset_time=0;//in milliseconds



#define TEMP_PIN 5

OneWire oneWirePin(TEMP_PIN);


DallasTemperature sensors(&oneWirePin);


void show(int x) //format: "#: time temp " 
{
  Serial.print(x);
  Serial.print(": ");
  Serial.print(t_time);
  Serial.print(" ");
  Serial.print(current_temp[x]);
  Serial.print(" ");
}

void setup(void) {
  
  Serial.begin(9600);
  sensors.begin();
  //gives time to get ready
  
  
//  delay(1000*30);
  Serial.print("Get ready and clear output");
  //delay(1000*5);
  offset_time=millis();
}



void loop() 
{
  sensors.requestTemperatures();
  t_time= (millis()-offset_time)/1000; //remember, we dont "t_time+=" because millis() keeps track

  for (cnt=0;cnt<5;cnt++)
  {
    current_temp[cnt]=sensors.getTempCByIndex(cnt);
    
    if (done[cnt]==-1);//does nothing
    
  
     else if (current_temp[cnt]<0.1)
    {
      done[cnt]=-1;
      current_temp[cnt]=0.0;
      show(cnt);
    }
    /*
    else if (done[cnt]>120) //decide whether you want this 
    {
      done[cnt]=-1;
      current_temp[cnt]=0.0;
      show(cnt);
    }
    else if (current_temp[cnt]<0.3) // and this goes along with it
    {
      done[cnt]+=wait/1000;
    }
    */
    else if ( abs(last_temp[cnt]-current_temp[cnt]) > 0.20 )
    {
        show(cnt);
        last_temp[cnt]=current_temp[cnt];
    }
  }
  delay(wait);
}
