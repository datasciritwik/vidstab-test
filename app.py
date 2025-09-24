import av
import cv2
import numpy as np
import streamlit as st
from vidstab import VidStab
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

st.title("Real-Time Video Stabilization with VidStab")

# Initialize stabilizer once
stabilizer = VidStab()

class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        
        stabilized_frame = stabilizer.stabilize_frame(input_frame=img, smoothing_window=30)
        if stabilized_frame is None:
            stabilized_frame = img  # fallback for first few frames
        
        return stabilized_frame

webrtc_streamer(key="stabilization", video_transformer_factory=VideoTransformer)