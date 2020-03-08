#include <ros.h>
#include <std_msgs/Empty.h>

const int en1 = 5;
const int in11 = 6;
const int in12 = 7;

const int en2 = 8;
const int in21 = 9;
const int in22 = 10;

ros::NodeHandle nh;
void backword(const std_msgs::Empty& toggle_msg)
{
  analogWrite(en1, 150);
  digitalWrite(in11,LOW);
  digitalWrite(in12,HIGH);
  
  analogWrite(en2, 150);
  digitalWrite(in21,LOW);
  digitalWrite(in22,HIGH);
  }
 void forword(const std_msgs::Empty& toggle_msg)
{
  analogWrite(en1, 150);
  digitalWrite(in11,HIGH);
  digitalWrite(in12,LOW);
  
  analogWrite(en2, 150);
  digitalWrite(in21,HIGH);
  digitalWrite(in22,LOW);
  }
 void left(const std_msgs::Empty& toggle_msg)
{
  analogWrite(en1, 150);
  digitalWrite(in11,HIGH);
  digitalWrite(in12,LOW);
  
  analogWrite(en2, 0);
  digitalWrite(in21,HIGH);
  digitalWrite(in22,LOW);
  }
ros::Subscriber<std_msgs::Empty> avant("bw", &backword);
ros::Subscriber<std_msgs::Empty> arriere("fw", &forword);
ros::Subscriber<std_msgs::Empty> sub("lw", &left);
void setup() {
  // put your setup code here, to run once:
  pinMode(en1, OUTPUT);
  pinMode(in11, OUTPUT);
  pinMode(in12, OUTPUT);
  
  pinMode(en2, OUTPUT);
  pinMode(in21, OUTPUT);
  pinMode(in22, OUTPUT);

  nh.initNode();
  nh.subscribe(arriere);
  nh.subscribe(avant);
  nh.subscribe(sub);
}

void loop(){
   nh.spinOnce();
   delay(1);
}
