# ROS
communication between ros subscriber and publisher via  ros topic 

1.  Ubuntu install of ROS Melodic:
http://wiki.ros.org/melodic/Installation/Ubuntu

2.  Creating a workspace for catkin:
http://wiki.ros.org/catkin/Tutorials/create_a_workspace

3. RPLidar ROS Package:
https://github.com/robopeak/rplidar_ros

* before running file_name.launch make sure run “source devel/setup.bash” in a same  directory .

4. Hector SLAM ROS Package:
https://github.com/tu-darmstadt-ros-pkg/hector_slam

Install RPLidar node and Hector SLAM
cd $HOME/catkin_ws/src
git clone https://github.com/Slamtec/rplidar_ros.git
git clone https://github.com/tu-darmstadt-ros-pkg/hector_slam.git
Using your favourite editor open Hector SLAM’s launch file which can be found at $HOME/catkin_ws/src/hector_slam/hector_mapping/launch/mapping_default.launch and modify the “base_frame”, “odom_frame” and commented out “tf” lines to look like below:
<arg name="base_frame" default="base_link"/>
<arg name="odom_frame" default="base_link"/>

<node pkg="tf" type="static_transform_publisher" name="base_to_laser_broadcaster" args="0 0 0 0 0 0 base_link laser 100" />
Edit Hector SLAM’s hector_imu_attitude_to_tf/launch/example.launch file which can be found at $HOME/catkin_ws/src/hector_slam/hector_imu_attitude_to_tf/launch/example.launch and change it to consume IMU data from the flight controller (via mavros) by replacing “thumper_imu” with “/mavros/imu/data” so that it looks like below:
<remap from="imu_topic" to="/mavros/imu/data" />
Edit Hector SLAM’s tutorial.launch file which can be found at $HOME/catkin_ws/src/hector_slam/hector_slam_launch/launch/tutorial.launch and change the “use_sim_time” line to look like below:
<param name="/use_sim_time" value="false"/>
Continue editing the tutorial.launch and add a new line (just below the existing include line) so that the example.launch file modified above is included:
<include file="$(find hector_imu_attitude_to_tf)/launch/example.launch"/>
6. sudo apt-get install qt4-default
7. $me_admin:~$cd catkin_ws
   $me_admin:~/catkin_ws$ catkin_make
8. roslaunch rplidar_ros rplidar.launch
9.roslaunch hector_slam_launch tutorial.launch
10. http://ardupilot.org/dev/docs/ros-slam.html


ls -l /dev |grep ttyUSB
sudo chmod 666 /dev/ttyUSB0
roslaunch rplidar_ros view_rplidar.launch
roslaunch rplidar_ros rplidar.launch

# multiple_connection
gedit .bashrc
source .bashrc 
export ROS_MASTER_URI=http://ubiquityrobot.local:11311/
export ROS_IP=192.168.0.108

$$$$ https://husarion.com/tutorials/ros-tutorials/1-ros-introduction/
https://husarion.com/tutorials/ros-tutorials/9-map-navigation/


@@@@@@@@@@@@@@
https://www.theconstructsim.com/ros-projects-exploring-ros-using-2-wheeled-robot-part-1/
https://bitbucket.org/theconstructcore/two-wheeled-robot-motion-planning/src/master/scripts/
https://bitbucket.org/theconstructcore/two-wheeled-robot-simulation/src/master/

@##@##
https://husarion.com/tutorials/ros-tutorials/9-map-navigation/
https://github.com/husarion/tutorial_pkg
https://answers.ros.org/question/199818/problems-about-gmapping-under-the-environment-roshydroturtlebot2rplidar/
http://geduino.blogspot.com/2015/04/gmapping-and-rplidar.html
https://github.com/geduino-foundation/rplidar_ros
https://husarion.com/tutorials/ros-projects/security-guard-robot/

IMU
https://atadiat.com/en/e-ros-imu-and-arduino-how-to-send-to-ros/
https://topic.alibabacloud.com/a/application-of-mpu6050-in-ros_8_8_10276014.html
