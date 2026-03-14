# ROS2 Maze Navigation Robot

This project simulates a **differential drive robot in ROS2 Humble using Gazebo 11** that navigates a maze using **LiDAR-based obstacle avoidance and wall following**.

## Features
- ROS2 Humble robot simulation
- Gazebo environment
- Differential drive robot
- LiDAR sensor processing
- Obstacle avoidance navigation

## Project Structure
bumper_bot/
├── launch/
├── urdf/
├── worlds/
├── models/
├── scripts/
├── package.xml
├── setup.py
└── CMakeLists.txt

## Run the Simulation

Build workspace:
colcon build
source install/setup.bash
Launch Gazebo:
ros2 launch bumper_bot city_world.launch.py
Run navigation node:
## Author

Modini Vardhan  
https://github.com/Modini-Vardhan-29

ros2 run bumper_bot obstacle_avoidance
