#include <ros.h>
#include <std_msgs/Empty.h>

ros::NodeHandle nh;

void down( const std_msgs::Empty& toggle_msg){
  digitalWrite(1, LOW); 
  digitalWrite(2, HIGH);  
  

  digitalWrite(7, HIGH); 
  digitalWrite(8, LOW);  
}
  void up( const std_msgs::Empty& toggle_msg){
  digitalWrite(1, HIGH); 
  digitalWrite(2, LOW);  
   

  digitalWrite(8, HIGH); 
  digitalWrite(7, LOW);  
  
}


ros::Subscriber<std_msgs::Empty> avant("av", &up);
ros::Subscriber<std_msgs::Empty> arriere("ar", &down);

void setup(){
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(1, OUTPUT);
  pinMode(2, OUTPUT); 
  nh.initNode();
  nh.subscribe(arriere);
  nh.subscribe(avant);

}

void loop(){
   nh.spinOnce();
   delay(1);
}
