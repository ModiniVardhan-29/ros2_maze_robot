import os

from launch import LaunchDescription
from launch.actions import ExecuteProcess, TimerAction
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    pkg_path = get_package_share_directory('bumper_bot')
    world = os.path.join(pkg_path, 'worlds', 'maze.world')
    urdf = os.path.join(pkg_path, 'urdf', 'bumper_bot.urdf')

    # Start Gazebo SERVER only (no GUI)
    gzserver = ExecuteProcess(
        cmd=[
            'gzserver',
            world,
            '-s', 'libgazebo_ros_init.so',
            '-s', 'libgazebo_ros_factory.so'
        ],
        output='screen'
    )

    # Spawn robot
    spawn = TimerAction(
        period=5.0,
        actions=[
            Node(
                package='gazebo_ros',
                executable='spawn_entity.py',
                arguments=[
                    '-entity', 'bumper_bot',
                    '-file', urdf,
                    '-x', '0',
                    '-y', '0',
                    '-z', '0.3'
                ],
                output='screen'
            )
        ]
    )

    return LaunchDescription([
        gzserver,
        spawn
    ])

