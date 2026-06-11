import os
from flask import Flask, render_template, request, jsonify
from PIL import Image

from model import load_model, predict_disease
from gradcam import generate_gradcam
from severity import estimate_severity
from treatment import get_treatment

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs('uploads', exist_ok=True)
os.makedirs('static', exist_ok=True)

print("Loading AI model... please wait")
model = load_model()
print("Model is ready!")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(image_path)

    image = Image.open(image_path).convert('L').resize((224, 224))
    pixels = list(image.getdata())
    brightness = sum(pixels) / len(pixels)

    prediction   = predict_disease(image_path, model)
    generate_gradcam(image_path, model)
    severity     = estimate_severity(prediction['confidence'], brightness)
    treatment_en = get_treatment(prediction['disease'], lang='en')
    treatment_hi = get_treatment(prediction['disease'], lang='hi')

    return jsonify({
        'disease':      prediction['disease'],
        'confidence':   prediction['confidence'],
        'severity':     severity['severity'],
        'yield_loss':   severity['yield_loss'],
        'treatment_en': treatment_en,
        'treatment_hi': treatment_hi,
        'heatmap':      '/static/heatmap.jpg'
    })

if __name__ == '__main__':
    app.run(debug=True)
