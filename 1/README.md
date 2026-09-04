# 🏎️ Robot Car Model (Lightning McQueen)

A ROS 2 package containing a custom **Xacro/URDF** model of a car robot inspired by Lightning McQueen. It configures Gazebo Sim plugins for motion control and camera telemetry, launching alongside **RViz2** for real-time visualization.

---

## 📋 Prerequisites & Installation

### Environment
* **OS:** Ubuntu 24.04 LTS
* **ROS 2 Version:** ROS 2 Jazzy Jalisco
* **Simulation Engine:** Gazebo Sim 8.11.0 (Harmonic)
* **Language:** Python 3.12.3

### Install Dependencies
Run the following command to install all required ROS 2 and Gazebo integration packages:

```bash
sudo apt update && sudo apt install -y \
  ros-jazzy-ros-gz \
  ros-jazzy-xacro \
  ros-jazzy-robot-state-publisher \
  ros-jazzy-rviz2
```

### ⚙️ Features

* Custom Xacro Architecture: Modular visual, collision, and inertial properties.

* Motion Plugin: Integrated gz-sim-diff-drive-system for differential velocity control (/cmd_vel).

* Camera Sensor Plugin: Integrated gz-sim-sensors-system streaming RGB feeds (/camera/image_raw).

* Visualization: Pre-configured RViz2 node launched simultaneously to monitor robot tf transforms and camera topics.

### 🚀 Usage Guide
#### 1. Set Up Workspace

Create and navigate to your ROS 2 workspace:
``` bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
```
#### 2. Clone Repository

Clone this package into your src directory:
```bash
git clone https://github.com/Abdulrahman-Mostafa53/robotics-transformation
```
**and only keep contents of folder 1**

#### 3. Build & Source

Build the workspace using colcon and source the environment overlay:

``` bash
cd ~/ros2_ws
colcon build
source install/setup.bash
```

#### 4. Launch Simulation & RViz

Launch Gazebo Sim, spawn the model, and open RViz2 with a single command:

``` bash 
ros2 launch robot_desc gazebo.launch.py
```

## 📡 ROS 2 Interfaces

### Published Topics
* **`/camera/image`** (`sensor_msgs/msg/Image`) — Live RGB video feed streaming from the robot's camera sensor.
* **`/camera/info`** (`sensor_msgs/msg/CameraInfo`) — Camera intrinsic calibration parameters and frame metadata.
* **`/joint_states`** (`sensor_msgs/msg/JointState`) — Real-time position and velocity updates for robot joints and wheels.
* **`/tf`** (`tf2_msgs/msg/TFMessage`) — Dynamic coordinate frame transformations across the robot's kinematic chain.
* **`/tf_static`** (`tf2_msgs/msg/TFMessage`) — Static coordinate frame transformations (e.g., fixed camera mount relative to base_link).
* **`/robot_description`** (`std_msgs/msg/String`) — Parsed URDF/Xacro robot description used by RViz2 and state publishers.

### Subscribed Topics
* **`/cmd_vel`** (`geometry_msgs/msg/Twist`) — Velocity commands controlling linear and angular robot movement.
