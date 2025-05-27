# 🧠 SilentSpeech AI

SilentSpeech AI is a real-time lip-reading system that converts silent video into readable text — designed for communication in noisy environments or for the speech-impaired.

---

## 📝 Problem Statement

In situations where speech is impractical — due to noise, disability, or silence requirements — communication is severely restricted. This project aims to bridge that gap using deep learning to interpret lip movements and convert them into text in real-time.

---

## 💡 Approach & Solution

We use a combination of computer vision and deep learning to:
1. Capture video feed using OpenCV.
2. Use Mediapipe to detect and extract lip region.
3. Feed lip sequences to a trained deep learning model.
4. Display real-time predictions in a user interface.

---

## 🔑 Features

- Real-time webcam-based lip reading.
- Converts silent video to live text.
- Designed for accessibility and noisy environments.
- Lightweight and local (privacy-focused).

---

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** Streamlit
- **CV/AI:** OpenCV, Mediapipe, PyTorch
- **Model:** CNN-RNN (LipNet-style architecture)
- **UI:** Streamlit, optional HTML overlay

---

## 🖼️ Screenshots

_Add screenshots to `assets/screenshots/` and display here:_

![Demo](assets/screenshots/demo.png)

---

## 🚀 Run Instructions

```bash
# Clone repo
git clone https://github.com/yourusername/silentspeech-ai.git
cd silentspeech-ai

# Setup environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
```

---

## 📁 Folder Structure

```
silentspeech-ai/
├── app.py
├── model/
├── ui/
├── assets/
├── requirements.txt
└── README.md
```

---

## 📬 Contact

**Name**: Saranyaa  
**Email**: your-email@example.com  
**GitHub**: [yourusername](https://github.com/yourusername)