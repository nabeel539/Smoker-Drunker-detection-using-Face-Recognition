int ALCOHOL_sensor = A1;
int ALCOHOL_detected;


int smoke_sensor = A0;
int smoke_detected;

void setup()
{
  Serial.begin(9600);
  pinMode(ALCOHOL_sensor, INPUT);

  pinMode(smoke_sensor, INPUT);

}
void loop()
{

  ALCOHOL_detected = alchol();
  Serial.println(ALCOHOL_detected);
  delay(1000);
  smoke_detected = smoke();
  Serial.println(smoke_detected);
  delay(1000);
  
//  if (ALCOHOL_detected == 1 || smoke_detected == 1)
//  {
//    if (smoke_detected == 1)
//    {
//      Serial.println("S-1");
//    }
//
//
//    if(ALCOHOL_detected == 1)
//    {
//      Serial.println("A-1");
//
//    }
//
//  }
//  else
//  {
//     Serial.println("S-0");
//     Serial.println("A-0");
//
//  }

  delay(1000);
   
}
// Digital value of smoke

int smoke(){
  int val=analogRead(smoke_sensor);
  if(val>180 && val <320){
    
    return 1;
    }else{
      return 0;
      }
  
  }

 // Digital value of alchol
  int alchol(){
  int val=analogRead(ALCOHOL_sensor);
  if(val>350){
    
    return 1;
    }else{
      return 0;
      }
  
  }
