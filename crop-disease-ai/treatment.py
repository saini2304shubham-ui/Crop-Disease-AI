TREATMENTS = {
    "Bacterial Blight": {
        "en": "Apply copper-based bactericides. Remove infected leaves immediately. Avoid overhead irrigation. Use disease-resistant varieties next season.",
        "hi": "तांबे आधारित बैक्टीरीसाइड लगाएं। संक्रमित पत्तियों को तुरंत हटाएं। ऊपर से सिंचाई न करें।"
    },
    "Leaf Rust": {
        "en": "Apply fungicides like Mancozeb or Propiconazole. Remove and burn infected crop debris. Ensure proper spacing between plants for airflow.",
        "hi": "मैनकोज़ेब जैसे फफूंदनाशक लगाएं। संक्रमित फसल अवशेषों को जलाएं। पौधों के बीच उचित दूरी बनाएं।"
    },
    "Powdery Mildew": {
        "en": "Spray sulfur-based fungicides or neem oil. Improve ventilation around plants. Avoid excessive nitrogen fertilizer.",
        "hi": "सल्फर आधारित फफूंदनाशक या नीम का तेल स्प्रे करें। पौधों के आसपास हवादार वातावरण बनाएं।"
    },
    "Healthy": {
        "en": "Your crop looks healthy! Continue regular monitoring, maintain proper irrigation, and ensure balanced fertilization.",
        "hi": "आपकी फसल स्वस्थ दिखती है! नियमित निगरानी जारी रखें और उचित सिंचाई बनाए रखें।"
    }
}

def get_treatment(disease, lang="en"):
    advice = TREATMENTS.get(disease, TREATMENTS["Healthy"])
    return advice.get(lang, advice["en"])
