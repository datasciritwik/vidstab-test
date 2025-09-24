import streamlit as st
import cv2
from vidstab import VidStab

st.title("Live Video Stabilization (Webcam)")

# Create VidStab object
stabilizer = VidStab()

# Streamlit camera input (captures snapshots, not continuous stream)
frame_window = st.image([])

camera = st.camera_input("Start camera")

if camera:
    # Convert snapshot into cv2 image
    file_bytes = np.asarray(bytearray(camera.read()), dtype=np.uint8)
    frame = cv2.imdecode(file_bytes, 1)

    # Stabilize the frame
    stabilized_frame = stabilizer.stabilize_frame(input_frame=frame, smoothing_window=30)

    if stabilized_frame is None:
        stabilized_frame = frame  # fallback

    # Show stabilized frame
    frame_window.image(cv2.cvtColor(stabilized_frame, cv2.COLOR_BGR2RGB))