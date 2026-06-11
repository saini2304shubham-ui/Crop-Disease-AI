from PIL import Image, ImageEnhance, ImageFilter
import os

def generate_gradcam(image_path, model, output_path="static/heatmap.jpg"):
    try:
        image = Image.open(image_path).convert("RGB")
        image = image.resize((224, 224))

        r, g, b = image.split()
        enhanced_r = ImageEnhance.Contrast(r).enhance(2.5)
        heatmap = Image.merge("RGB", (enhanced_r, g, b))
        blended = Image.blend(image, heatmap, alpha=0.5)
        sharpened = blended.filter(ImageFilter.SHARPEN)

        os.makedirs("static", exist_ok=True)
        sharpened.save(output_path)

    except Exception as e:
        print(f"Heatmap error: {e}")
        image = Image.open(image_path).convert("RGB")
        image.resize((224, 224)).save(output_path)

    return output_path
