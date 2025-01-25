from ultralytics import YOLO
import cv2

model = YOLO('last.pt')
results = model(source="videoplayback (2).mp4",imgsz = 640, show=False, save=True)