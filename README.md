# Pedestrian Simulator (Pedsim_ROS) - Distracted Node

This repository presents the library "Pedestrian Simulator (Pedsim_ROS) - Distracted Node" for a pedestrians simulator with distracted behavior based on the Pedsim_ROS library which is also based on the Helbing social force model. The implementation of the library is based on the addition of nodes and distractor topics to show different behaviors of the agents.


### Features
- Distracted nodes and topics for distracted behaviour in agents

### Requirements
- ROS with the visualization stack (currently tested on `noetic` )
- C++11 compiler
- Python 2.8+

### Installation

```
cd [workspace]/src
git clone https://github.com/npulidog/pedsim_ros_distracted_node.git
cd pedsim_ros_distracted_node
git submodule update --init --recursive
cd ../..
catkin build -c  # or catkin_make
```
### Sample usage
```
roslaunch pedsim_simulator Pasillo.launch
```
```
roslaunch pedsim_simulator cruz.launch
```

### Licence
The core `libpedsim` is licensed under LGPL. The ROS integration and extensions are licensed under BSD.

### Developers
* Nicolas Pulido Gerena
* Camilo Ernesto Campo Pacheco


### Contributors
* Juan Sebastian Hernandez Reyes
* Jose Manuel Fajardo

The package is a **work in progress** mainly used in research prototyping. Pull requests and/or issues are highly encouraged.

### Acknowledgements
These packages have been developed during our degree work (2022)
