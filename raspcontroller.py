import streamlit as st
from PIL import Image
import cv2
import numpy as np
from ultralytics import YOLO
import RPi.GPIO as GPIO
from picamera2 import Picamera2
import time

GPIO.setmode(GPIO.BCM)
MOTOR_PIN = 18
ACTUATOR_PIN = 23
GPIO.setup(MOTOR_PIN, GPIO.OUT)
GPIO.setup(ACTUATOR_PIN, GPIO.OUT)
GPIO.output(MOTOR_PIN, GPIO.HIGH)
GPIO.output(ACTUATOR_PIN, GPIO.LOW)

picam = Picamera2()
picam.configure(picam.create_still_configuration())
picam.start()

model = YOLO("models/best.pt")

st.title("Mini Conveyor Defect Detection")
st.write("Real-time defect detection using Raspberry Pi and YOLO")
image_placeholder = st.empty()
status_placeholder = st.empty()

def capture_image():
    image = picam.capture_array()
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return image

def process_image(image):
    results = model.predict(image, conf=0.5)
    for result in results:
        boxes = result.boxes
        for box in boxes:
            label = result.names[int(box.cls)]
            confidence = box.conf.item()
            return label, confidence
    return "plastic", 1.0

def control_conveyor(label):
    if label in ["plasticdefected", "metaldefected"]:
        GPIO.output(ACTUATOR_PIN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(ACTUATOR_PIN, GPIO.LOW)

try:
    while True:
        image = capture_image()
        label, confidence = process_image(image)
        print(label)
        control_conveyor(label)
        image_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        image_placeholder.image(image_pil, caption=f"Detection: {label} ({confidence:.2f})")
        status_placeholder.write(f"Detection: {label}")
        cv2.imwrite(f"data/sample_images/capture_{int(time.time())}.jpg", image)
        time.sleep(1)
except KeyboardInterrupt:
    st.write("Stopping conveyor and cleaning up...")
finally:
    GPIO.output(MOTOR_PIN, GPIO.LOW)
    GPIO.cleanup()
    picam.stop()