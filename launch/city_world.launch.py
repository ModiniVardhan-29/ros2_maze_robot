import os

from launch import LaunchDescription
from launch.actions import TimerAction, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    pkg_path = get_package_share_directory('bumper_bot')
    gazebo_pkg = get_package_share_directory('gazebo_ros')

    world_path = os.path.join(pkg_path, 'worlds', 'maze.world')
    urdf_path = os.path.join(pkg_path, 'urdf', 'bumper_bot.urdf')

    # Start Gazebo with ROS plugins
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(gazebo_pkg, 'launch', 'gazebo.launch.py')
        ),
        launch_arguments={
            'world': world_path
        }.items()
    )

    # Spawn robot after Gazebo starts
    spawn_robot = TimerAction(
        period=5.0,
        actions=[
            Node(
                package='gazebo_ros',
                executable='spawn_entity.py',
                arguments=[
                    '-entity', 'bumper_bot',
                    '-file', urdf_path,
                    '-x', '0.0',
                    '-y', '0.0',
                    '-z', '0.3'
                ],
                output='screen'
            )
        ]
    )

    return LaunchDescription([
        gazebo,
        spawn_robot
    ])

