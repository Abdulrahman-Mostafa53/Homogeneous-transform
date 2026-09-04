# Homogeneous Transformation for Mobile Robotics

This project applies 3D **Homogeneous Transformations** to map obstacle coordinates detected in a camera's frame of reference to a robot's base frame.

## Overview
To navigate safely, a robot must map environmental obstacles (seen via sensor/camera) into its own coordinate system. This repository provides a light implementation of performing 3D rigid body transformations ($4 \times 4$ homogeneous matrices).

## Project Structure

* **`matrix.py`**: Custom matrix implementation built from scratch.
* **`main.py`**: constructs the $4 \times 4$ homogeneous transformation matrix, and transforms the 3D points.

## Quick Start

### 1. Configure Input Points
Open `main.py` and define your target obstacle coordinates relative to the camera in the `points` variable:

```python
# Example: 3D coordinates (x, y, z) relative to camera frame
points = [
    [2.0, 0.0, -0.2],
    [3.5, 1.0, -0.3],
    [1.5, -0.8, -0.1]
]
```

### 2. Run the Script

Execute the main script using Python 3:

```Bash
python main.py