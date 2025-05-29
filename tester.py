import streamlit as st
from PIL import Image
import cv2
import numpy as np
from ultralytics import YOLO

# Load model and classes
MODEL_PATH = r"C:\Users\adnan\runs\detect\train\weights\best.pt"
model = YOLO(MODEL_PATH)

st.title("🧠 YOLO Object Detection App")
st.write("Upload an image and view detections using your custom-trained YOLO model.")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Run Detection"):
        # Convert to OpenCV format
        img_array = np.array(image)
        img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

        # Inference
        results = model(img_bgr)[0]

        # Plot with boxes
        annotated_frame = results.plot()

        st.image(annotated_frame, caption="Detection Result", use_column_width=True)

        st.subheader("Detected Objects:")
        for box in results.boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            class_name = model.names[cls_id]
            st.write(f"- {class_name} ({conf:.2f})")
