from PIL import Image
import random

def detect_fake_image(image):

    # Simulated deepfake detection
    result = random.randint(40, 95)

    if result > 70:
        verdict = "Image appears authentic"
    else:
        verdict = "Possible AI-generated image"

    return {
        "score": result,
        "verdict": verdict
    }