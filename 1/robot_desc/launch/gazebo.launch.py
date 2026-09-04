import launch
from launch.actions import IncludeLaunchDescription,DeclareLaunchArgument,SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
import os


def generate_launch_description():
    # define the required paths in this package
    this_pkg_share = FindPackageShare(package="robot_desc").find("robot_desc")
    car_model_path = os.path.join(this_pkg_share, "urdf/car.urdf.xacro")
    gz_bridge_path = os.path.join(this_pkg_share,'config','gz_bridge.yaml')
    rviz_config_path = os.path.join(this_pkg_share, "rviz/config.rviz")

    # define ros_gz_sim package required paths
    gazebo_sim_pkg_share_path = FindPackageShare(package="ros_gz_sim").find("ros_gz_sim")
    gazebo_sim_launch_path = os.path.join(gazebo_sim_pkg_share_path,'launch','gz_sim.launch.py')

    # set up where gazebo looks for resources
    set_gz_resource_path = SetEnvironmentVariable(name = "GZ_SIM_RESOURCE_PATH",value=os.path.dirname(this_pkg_share))
    
    # launch the gazebo sim launch file in using this launch file
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(gazebo_sim_launch_path),
                launch_arguments = {'gz_args' : f'-r empty.sdf' , "on_exit_shutdown":"true"}.items()
    )

    # define robot_state_publisher_node and give it the car xacro model 
    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[
            {"robot_description": Command(["xacro ", LaunchConfiguration("model")])}
        ],
    )

    # define joint_state_publsiher_node
    joint_state_publsiher_node = Node(
        package="joint_state_publisher",
        executable="joint_state_publisher",
        name="joint_state_publisher",
    )

    # define the node that spawns the robot in gazebo sim
    spawn_entity_node = Node(
        package="ros_gz_sim",
        executable="create",
        arguments=["name","car","-topic","robot_description",'-z','0.3'],
        output = "screen"
    )

    # define the node resposible for bridging topics between gazebo and ros (provide it with the config file as a node parameter)
    ros_gz_bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        arguments=['--ros-args','-p',f'config_file:={gz_bridge_path}'],
    )

    # define the node that runs rviz 
    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        arguments=["-d", LaunchConfiguration("rvizconfig")],
    )

    # run all nodes and the gazebo launch file

    return launch.LaunchDescription(
        [ 
            set_gz_resource_path,
            ros_gz_bridge,
            gazebo,
            DeclareLaunchArgument(
                name="rvizconfig",
                default_value=rviz_config_path,
                description="Absolute path to rviz config file",
            ),
            DeclareLaunchArgument(
                name="model",
                default_value=car_model_path,
                description="Absolute path to car urdf file",
            ),
            rviz_node,
            launch.actions.ExecuteProcess(cmd = ['gazebo','--verbose','-s','libgazebo_ros_init.so','-s','libgazebo_ros_factory.so'],output= "screen"),
            joint_state_publsiher_node,
            robot_state_publisher_node,
            spawn_entity_node,
        ]
    )
