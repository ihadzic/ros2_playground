from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(package='play', executable='my_pub', name='ilija_pub')
    ])
