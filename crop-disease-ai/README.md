# 🌾 FarmAI — Crop Disease Detector

An AI-powered web application that helps smallholder farmers in rural India
diagnose crop diseases instantly from a smartphone photo.

## 🎯 Problem Statement
Smallholder farmers in rural India lose 20-40% of their yield every year
due to undetected or misdiagnosed crop diseases. They have no access to
agricultural experts and cannot afford lab testing.

## 💡 Solution
FarmAI is a multi-model AI pipeline that allows farmers to upload a photo
of their crop and instantly receive a full diagnosis report.

## ✨ Features
- 🔍 Crop disease detection using Computer Vision
- 🔬 Explainability heatmap showing where AI focused
- 📊 Severity estimation using Classical ML (Random Forest)
- 📉 Yield loss percentage prediction
- 💊 Treatment guidance in English and Hindi
- 📱 Mobile friendly for smartphone use

## 🧠 AI Pipeline
| Component | Technology |
|---|---|
| Disease Detection | Computer Vision (Color Analysis) |
| Explainability | Image Heatmap (Pillow) |
| Severity Estimation | Random Forest (scikit-learn) |
| Treatment Advice | NLP Bilingual Database |
| Web Server | Flask (Python) |

## 🚀 How to Run

### 1. Install libraries
```
pip install flask pillow scikit-learn numpy
```

### 2. Run the app
```
python app.py
```

### 3. Open browser
```
http://localhost:5000
```

## 📁 Project Structure
```
crop-disease-ai/
├── app.py              — Main Flask web server
├── model.py            — Disease detector
├── gradcam.py          — Explainability heatmap
├── severity.py         — Classical ML severity estimator
├── treatment.py        — NLP treatment advice
├── templates/
│   └── index.html      — Farmer web interface
├── static/
│   └── style.css       — Page styling
└── uploads/            — Uploaded images
```

## 🌍 Impact
- Targets 100+ million smallholder farmers in India
- Bilingual support in English and Hindi for rural accessibility
- Works on any smartphone with a camera
- No internet dependency for treatment advice
- Explainable AI so farmers understand the diagnosis

## 👨‍💻 Built With
- Python 3.11
- Flask
- scikit-learn
- Pillow
- NumPy

## 🏆 Built for Hackathon
This project was built as part of a hackathon with the objective of
creating an explainable multi-model AI pipeline for crop disease
detection targeting rural farmers in India.
