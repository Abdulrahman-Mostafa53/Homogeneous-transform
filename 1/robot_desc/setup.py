from setuptools import find_packages, setup

package_name = 'robot_desc'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name +"/meshes", ['meshes/car.glb','meshes/wheel.glb','meshes/camera.glb']),
        ('share/' + package_name +"/launch", ['launch/gazebo.launch.py']),
        ('share/' + package_name +"/urdf", ['urdf/car.urdf.xacro']),
        ('share/' + package_name +"/rviz", ['rviz/config.rviz']),
        ('share/' + package_name +"/config", ['config/gz_bridge.yaml'])

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='abdulrahman',
    maintainer_email='abdulrahmanmostafa1101@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
