from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    imu_node = Node(
        package='wit_ros2_imu',
        executable='wit_ros2_imu',
        name='imu',
        remappings=[('/wit/imu', '/imu/data')],
        parameters=[{'port': '/dev/ttyIMU'},
                    {"baud": 9600}],
        output="screen"

    )

    rviz_display_node = Node(
        package='rviz2',
        executable="rviz2",
        output="screen"
    )

    return LaunchDescription(
        [
            imu_node,
            #rviz_display_node
        ]
    )