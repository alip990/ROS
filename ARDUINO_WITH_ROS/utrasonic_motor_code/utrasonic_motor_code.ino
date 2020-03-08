int trigPin = 11;      // trig pin of HC-SR04
int echoPin = 12;     // Echo pin of HC-SR04

const int en1 = 5;
const int in11 = 6;
const int in12 = 7;

const int en2 = 8;
const int in21 = 9;
const int in22 = 10;

long duration, distance;

void backword(void)
{
  analogWrite(en1, 150);
  digitalWrite(in11,LOW);
  digitalWrite(in12,HIGH);
  
  analogWrite(en2, 150);
  digitalWrite(in21,LOW);
  digitalWrite(in22,HIGH);
  }

void forword(void)
{
  analogWrite(en1, 150);
  digitalWrite(in11,HIGH);
  digitalWrite(in12,LOW);
  
  analogWrite(en2, 150);
  digitalWrite(in21,HIGH);
  digitalWrite(in22,LOW);
  }
void left(void)
{
  analogWrite(en1, 150);
  digitalWrite(in11,HIGH);
  digitalWrite(in12,LOW);
  
  analogWrite(en2, 0);
  digitalWrite(in21,HIGH);
  digitalWrite(in22,LOW);
  }
void right(void)
{
  analogWrite(en1, 0);
  digitalWrite(in11,HIGH);
  digitalWrite(in12,LOW);
  
  analogWrite(en2, 150);
  digitalWrite(in21,HIGH);
  digitalWrite(in22,LOW);
  }
void all_stop(void)
{
  analogWrite(en1, 0);
  analogWrite(en2, 0);
  }
void setup() {
  
  delay(random(500,2000));   // delay for random time
  Serial.begin(9600);
  pinMode(en1, OUTPUT);
  pinMode(in11, OUTPUT);
  pinMode(in12, OUTPUT);
  
  pinMode(en2, OUTPUT);
  pinMode(in21, OUTPUT);
  pinMode(in22, OUTPUT);
  
  pinMode(trigPin, OUTPUT);         // set trig pin as output
  pinMode(echoPin, INPUT);          //set echo pin as input to capture reflected waves
}

void loop() {

  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);   
  digitalWrite(trigPin, HIGH);     // send waves for 10 us
  delayMicroseconds(10);
  duration = pulseIn(echoPin, HIGH); // receive reflected waves
  distance = duration / 58.2;   // convert to distance
  delay(10);
    // If you dont get proper movements of your robot then alter the pin numbers
  if (distance > 19)            
  {
    forword();                                                
  }

  if (distance < 18)
  {
    all_stop();
    //delay(500);
    //backword();
    //delay(500);
    //all_stop();
    //delay(100);  
    //right();
    //delay(500);
  }

}
