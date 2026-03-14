from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-entity', 'bumper_bot',
                '-file', '/home/modini/bumper_ws/src/bumper_bot/urdf/bumper_bot.urdf'
            ],
            output='screen'
        )
    ])
