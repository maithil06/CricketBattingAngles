# Cricket Batting Angles Analysis

This repository contains a collection of Python scripts designed for analyzing cricket batting angles using pose estimation, primarily leveraging MediaPipe. It includes modules for pose detection, angle calculation, data logging, and even object detection with YOLO.

## Features

* **Real-time Pose Detection:** Utilizes MediaPipe for accurate human pose estimation from video streams or webcam.
* **Joint Angle Calculation:** Calculates angles between key body joints (e.g., elbow, knee, hip, shoulder) for both left and right sides.
* **Batting Angle Analysis (Side View):** Specifically designed scripts to analyze batting form from a side angle, logging joint angles to a CSV file.
* **Pose Rep Counter:** Includes a module that can be adapted for counting repetitions of exercises based on joint angles (e.g., bicep curls).
* **Object Detection:** Integration with YOLO for general object detection.
* **Movement Scoring:** Implements `fastdtw` for dynamic time warping to compare and score movement sequences.

## Installation

To run these scripts, you'll need Python and the following libraries. You can install them using pip:

```bash
pip install opencv-python mediapipe numpy pandas ultralytics scipy fastdtw
```
## Usage
The project consists of several independent scripts, each serving a specific purpose:

**PoseModule.py**
This is a core module containing the poseDetector class. It provides functionalities for finding human poses and calculating angles between specified landmarks.
To run the example in main():

```bash
python PoseModule.py
```
**(Note: Requires a video file named 1.mp4 in a PoseVideos folder, or modify ```bash cap = cv2.VideoCapture('PoseVideos/1.mp4')``` to your video path or 0 for webcam.)

```SideAngleViewTrain.py``` and ```SideAngleViewTest.py```
These scripts are designed for analyzing cricket batting angles from a side view. They process a video, detect poses, calculate various joint angles, and log this data to a CSV file (traindata.csv) for training or testing purposes.
To run:

```bash
python SideAngleViewTrain.py
# or
python SideAngleViewTest.py
```

**(Note: Both scripts process virat - Made with Clipchamp.mp4. Ensure this video file is in the same directory or update the path ```bash cap = cv2.VideoCapture('virat - Made with Clipchamp.mp4'```).)**

```counters.py```
A utility script containing the ```calculate_angle``` function, used by ```SideAngleViewTrain.py```, ```SideAngleViewTest.py```, and ```PoseModule.py```. This file is imported by other scripts.

```counter.py```
This script demonstrates a simple repetition counter using the PoseModule. It tracks a specific angle (e.g., right arm) and counts reps based on angle thresholds.
To run:

```bash 
python counter.py
```
**(Note: Uses webcam by default ```cap = cv2.VideoCapture(0)```.)**

```new.py```
A basic script for real-time pose detection using MediaPipe with a webcam feed.
To run:
```bash
python new.py
```

