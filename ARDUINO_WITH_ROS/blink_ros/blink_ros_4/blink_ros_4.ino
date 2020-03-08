#include <ros.h>
#include <std_msgs/Empty.h>

ros::NodeHandle nh;

void messageON( const std_msgs::Empty& toggle_msg){
  digitalWrite(8, HIGH);   // blink the led
  digitalWrite(13, HIGH);   // blink the led
}

void messageOFF( const std_msgs::Empty& toggle_msg){
  digitalWrite(8, LOW);   // blink the led
  digitalWrite(13, LOW);   // blink the led
}

ros::Subscriber<std_msgs::Empty> sub("led_ON", &messageON );
ros::Subscriber<std_msgs::Empty> sub("led_OFF", &messageOFF );

void setup()
{
  pinMode(8, OUTPUT);
  pinMode(13, OUTPUT);
  nh.initNode();
  nh.subscribe(sub);
}

void loop()
{
  nh.spinOnce();
  delay(1);
}
