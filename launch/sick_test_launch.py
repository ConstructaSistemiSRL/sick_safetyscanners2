from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="sick_safetyscanners2",
            executable="sick_safetyscanners2_node",
            name="sick_safetyscanners2_node",
            output="screen",
            emulate_tty=True,
            parameters=[
                {"frame_id": "scan",
                 "sensor_ip": "192.168.2.81",
                 "host_ip": "192.168.2.200",
                 "interface_ip": "0.0.0.0",
                 "host_udp_port": 6060,
                 "channel": 0,
                 "channel_enabled": True,
                 "skip": 0,
                 "angle_start": 0.0,
                 "angle_end": 0.0,
                 "time_offset": 0.0,
                 "general_system_state": True,
                 "derived_settings": True,
                 "measurement_data": True,
                 "intrusion_data": True,
                 "application_io_data": True,
                 "use_persistent_config": False,
                 "min_intensities": 0.0}
            ]
        ),
        Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="log",
        arguments=[],
        parameters=[]
        ),
        # Static TF
        Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            name="static_transform_publisher",
            output="log",
            arguments=["0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "1.0", "world", "scan"],
        )
    ])
