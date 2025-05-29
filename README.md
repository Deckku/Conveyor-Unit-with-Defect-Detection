# Mini Conveyor Unit with Defect Detection

## Description
A mini conveyor system powered by a Raspberry Pi 4 with a YOLO model for real-time defect detection. It classifies pieces as defective or non-defective using a camera feed. Validated in Factory IO simulation and implemented in a real-life prototype for automated quality control.

<img width="500" alt="Screenshot 2025-05-29 130803" src="https://github.com/user-attachments/assets/42f7f706-64dc-464b-a2be-aefd604cd40b" />

## Features
- **Defect Detection**: Utilizes a YOLO model to classify pieces as defective or non-defective based on visual inspection.
- **Raspberry Pi 4**: Serves as the processing unit for running the YOLO model and controlling the conveyor system.
- **Factory IO Simulation**: A virtual environment to test and validate the conveyor system and defect detection logic.
- **Real-Life Model**: A physical prototype that mirrors the simulated setup, demonstrating real-world applicability.
- **Real-Time Processing**: Processes images from a camera feed to make immediate decisions about piece quality.
- **Modular Design**: Easily adaptable for different types of defects or conveyor configurations.

  ![image](https://github.com/user-attachments/assets/807a655d-2480-4dfd-a6bc-4f506368ee06)


## Hardware Requirements
- Raspberry Pi 4 (4GB or 8GB RAM recommended)
- USB Webcam or Pi Camera Module for capturing images
- Conveyor Belt System (custom-built or off-the-shelf mini conveyor)
- GPIO-connected actuators/sensors (e.g., motors, proximity sensors) for conveyor control
- Power Supply suitable for the Raspberry Pi and conveyor components

## Software Requirements
- Raspberry Pi OS (latest version recommended)
- Python 3.8+
- OpenCV for image processing
- YOLO Model (pre-trained or custom-trained for defect detection)
- Factory IO (for simulation)
- Required Python libraries:
  - opencv-python
  - numpy
  - ultralytics (for YOLO implementation)
  - RPi.GPIO (for Raspberry Pi GPIO control)

## Installation
1. **Set Up Raspberry Pi**:
   - Install Raspberry Pi OS on the Raspberry Pi 4.
   - Update the system:
     ```bash
     sudo apt update && sudo apt upgrade
     ```
   - Install required Python libraries:
     ```bash
     pip install opencv-python numpy ultralytics RPi.GPIO
     ```

2. **Configure the YOLO Model**:
   - Download or train a YOLO model (e.g., YOLOv8) for defect detection.
   - Place the model weights (e.g., `yolo_defect_model.pt`) in the project directory.
   - Ensure the model is trained to recognize defective vs. non-defective pieces specific to your use case.

3. **Set Up Factory IO (Simulation)**:
   - Install Factory IO on a compatible PC.
   - Design a conveyor system in Factory IO with a camera and actuators to simulate the defect detection process.
   - Connect Factory IO to the Raspberry Pi via a compatible interface (e.g., Modbus or OPC UA) for real-time control.

4. **Real-Life Model Setup**:
   - Assemble the physical conveyor belt with a motor and sensors.
   - Connect the Raspberry Pi to the camera and GPIO pins for controlling the conveyor.
   - Ensure proper lighting for accurate image capture.



## Usage
1. **Simulation in Factory IO**:
   - Open the `conveyor_simulation.fio` file in Factory IO.
   - Run the `main.py` script on the Raspberry Pi to connect to Factory IO.
   - The system will simulate piece movement and defect detection, logging results to the console.

2. **Real-Life Model**:
   - Connect the camera and conveyor hardware to the Raspberry Pi.
   - Run the `main.py` script:
     ```bash
     python scripts/main.py
     ```
   - The system will process the camera feed, detect defects using the YOLO model, and control the conveyor to sort defective pieces.

3. **Example Workflow**:
   - The camera captures images of pieces on the conveyor.
   - The YOLO model processes each image to classify pieces as "defective" or "non-defective."
   - If a defect is detected, the Raspberry Pi triggers an actuator to divert the piece (e.g., to a reject bin).
   - Logs are generated for each detection event.

## Training the YOLO Model
- **Dataset**: Collect images of defective and non-defective pieces under consistent lighting conditions.
- **Labeling**: Use a tool like LabelImg to annotate images with bounding boxes and labels (e.g., "defective," "non-defective").
- **Training**: Train a YOLO model (e.g., YOLOv8) using the Ultralytics framework:
  ```bash
  yolo train model=yolov8n.pt data=dataset.yaml epochs=50 imgsz=640
  ```
- **Deployment**: Export the trained model weights and update the `models/` directory.

## Factory IO Simulation
- The Factory IO simulation replicates the conveyor system with a virtual camera and actuators.
- Use the simulation to test the YOLO model and conveyor control logic without physical hardware.
- Adjust parameters like conveyor speed and detection thresholds in the simulation for optimal performance.

## Real-Life Model Notes
- Ensure the camera is positioned to capture clear images of pieces.
- Calibrate the YOLO model for the specific defect types in your use case.
- Test the GPIO connections to ensure reliable control of the conveyor and actuators.

## Future Improvements
- Add a web interface for real-time monitoring and control.
- Implement multiple YOLO models for detecting different types of defects.
- Integrate with a cloud service for data logging and analytics.
- Enhance the real-life model with additional sensors (e.g., weight sensors) for more robust defect detection.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that any new features are tested in both the Factory IO simulation and the real-life model.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Sources
- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) for the YOLO implementation.
- [Factory IO](https://factoryio.com/) for simulation support.
- Raspberry Pi community for hardware and GPIO resources.



