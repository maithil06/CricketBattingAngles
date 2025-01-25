from ultralytics import YOLO
import cv2

cap = cv2.VideoCapture(0)

model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)

while True:
    ret, frame = cap.read()
    
    results = model.predict(source = frame, imgsz=640,show = True)
    cv2.waitKey(1)