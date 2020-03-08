#include <ros.h>
#include <std_msgs/Empty.h>

ros::NodeHandle nh;

void down( const std_msgs::Empty& toggle_msg){
  digitalWrite(6, LOW); 
  digitalWrite(7, HIGH);  
  analogWrite(5, 255); 

  digitalWrite(9, HIGH); 
  digitalWrite(10, LOW);  
  analogWrite(8, 255);  

 digitalWrite(13, HIGH); 
}
  void up( const std_msgs::Empty& toggle_msg){
  digitalWrite(6, HIGH); 
  digitalWrite(7, LOW);  
  analogWrite(5, 127); 

  digitalWrite(9, HIGH); 
  digitalWrite(10, LOW);  
  analogWrite(8, 127); 
}


ros::Subscriber<std_msgs::Empty> avant("av", &up);
ros::Subscriber<std_msgs::Empty> arriere("ar", &down);

void setup(){
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(1, OUTPUT);
  pinMode(2, OUTPUT); 
  pinMode(13, OUTPUT); 
  pinMode(10, OUTPUT); 
  pinMode(11, OUTPUT);
  nh.initNode();
  nh.subscribe(arriere);
  nh.subscribe(avant);

}

void loop(){
   nh.spinOnce();
   delay(1);
}
