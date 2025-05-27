import streamlit as st
from ui.video_capture import get_lip_frames
from model.predict import load_model, predict_lip_sequence

st.title("🧠 SilentSpeech AI")
st.write("Real-time lip reading AI that converts silent video to text.")

if st.button("Start Live Lip Reading"):
    st.info("Launching webcam... Press 'q' to stop.")
    get_lip_frames()