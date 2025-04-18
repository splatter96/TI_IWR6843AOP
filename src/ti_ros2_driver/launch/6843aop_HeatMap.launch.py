from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_path


def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package="ti_ros2_driver",
                namespace="ti_radar_0",
                executable="pcl_pub",
                parameters=[
                    {
                        "cfg_path": str(
                            get_package_share_path("ti_ros2_driver")
                            # / "cfg/RADheatmap.cfg"
                            # / "cfg/OnlyHeatmap.cfg"
                            / "cfg/heatmap_and_points.cfg"
                            # / "cfg/heatmap_and_points_4rx_2tx.cfg"
                        )
                    },  # cfg file for ti mmwave
                    {
                        "command_port": "/dev/ttyUSB0"
                    },  # if not known, run "ll/dev/serial/by-id" in terminal
                    {
                        "data_port": "/dev/ttyUSB1"
                    },  # if not known, run "ll/dev/serial/by-id" in terminal
                    {"frame_id": "ti_mmwaver_0"},  # frame id of published topic
                    {"topic": "ti_mmwave_0"},  # published topic name
                    {"output_RD_heatmap": False},  # if output Range-Doppler heatmap
                    {"output_RA_heatmap": True},  # if output Range-Azimuth heatmap
                    {"debug_mode": False},  # if using debug mode
                    {
                        "debug_log_path": str(
                            get_package_share_path("ti_ros2_driver")
                            / "debug/result_1.json"
                        )
                    },  # if using debug mode, the path of output debug log
                ],
                output="screen",
                emulate_tty=True,
            )
        ]
    )
