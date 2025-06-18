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

SideAngleViewTrain.py and SideAngleViewTest.py
These scripts are designed for analyzing cricket batting angles from a side view. They process a video, detect poses, calculate various joint angles, and log this data to a CSV file (traindata.csv) for training or testing purposes.
To run:
