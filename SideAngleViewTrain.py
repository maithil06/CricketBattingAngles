import cv2
import mediapipe as mp
import numpy as np
from counters import calculate_angle
import pandas as pd
import os
import glob

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

files = glob.glob('D:/python/AI trainer/train/*')
for f in files:
    os.remove(f)
    
video_pixels = np.array([1920,1080]) #pixels of video
cap = cv2.VideoCapture('virat - Made with Clipchamp.mp4')
file_path = 'D:/python/AI trainer/train/traindata.csv' #path to save data

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        success, image = cap.read()
        image = cv2.resize(image,(800,800))
        
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        
        results = pose.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        try:
            landmarks = results.pose_landmarks.landmark
            l_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y
            l_elbow = landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y
            l_wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y
            r_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y
            r_elbow = landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y
            r_wrist = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y
            l_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y
            l_knee = landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y
            l_ankle = landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y
            r_hip = landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y
            r_knee = landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y
            r_ankle = landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y
            
            l_angle = calculate_angle(l_shoulder,l_elbow,l_wrist)
            r_angle = calculate_angle(r_shoulder,r_elbow,r_wrist)
            l_angle1 = calculate_angle(l_hip,l_knee,l_ankle)
            r_angle1 = calculate_angle(r_hip,r_knee,r_ankle)
            
            n_angle = np.multiply(l_elbow,video_pixels).astype(int)
            m_angle = np.multiply(r_elbow,video_pixels).astype(int)
            o_angle = np.multiply(l_knee,video_pixels).astype(int)
            p_angle = np.multiply(r_knee,video_pixels).astype(int)
            
            one = (f"Left hand angle is : {l_angle}")
            two = (f"Right hand angle is : {r_angle}")
            three = (f"Left leg angle is : {l_angle1}")
            four = (f"Right leg angle is : {r_angle1}")
            
            data = pd.DataFrame({'Left Shoulder':l_angle,'Right Shoulder':r_angle,'Left Hip':l_angle1,'Right Hip':r_angle1},index=[0])
            data.to_csv(file_path,mode='a',header=False,)
            print(n_angle)
        except:
            pass
        
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2),  mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2))
        cv2.putText(image,str(l_angle),(n_angle),cv2.FONT_HERSHEY_COMPLEX,0.5,(250,250,250),3)
        cv2.putText(image,one,(1,25),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
        cv2.putText(image,str(r_angle),(m_angle),cv2.FONT_HERSHEY_COMPLEX,0.5,(250,250,250),2)
        cv2.putText(image,two,(1,50),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
        cv2.putText(image,str(l_angle1),(o_angle),cv2.FONT_HERSHEY_COMPLEX,0.5,(250,250,250),2)
        cv2.putText(image,three,(1,75),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
        cv2.putText(image,str(r_angle1),(p_angle),cv2.FONT_HERSHEY_COMPLEX,0.5,(250,250,250),2)
        cv2.putText(image,four,(1,100),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
        
        cv2.imshow('MediaPipe Pose', image)
        if cv2.waitKey(1) == 13:
            break