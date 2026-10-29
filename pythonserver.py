import colorsys
import os
from flask import Flask, Response
from PIL import ImageGrab

app = Flask(__name__)

# Coordinates to sample from the open reference image on screen
# By default, samples near center (adjust coordinates if needed)
SAMPLE_X = 500
SAMPLE_Y = 500
BOX_RADIUS = 12  # 12 px in all directions creates a 25x25 pixel cluster


def sample_screen_color(x, y, radius=12):
    """Samples a (2*radius + 1) square pixel cluster, averages RGB, and applies HSV saturation boost."""
    # Capture bounding box around coordinate
    bbox = (x - radius, y - radius, x + radius + 1, y + radius + 1)
    screenshot = ImageGrab.grab(bbox=bbox)

    pixels = list(screenshot.getdata())
    if not pixels:
        return "#1E90FF"  # Fallback ocean blue

    # Average the RGB cluster
    avg_r = sum(p[0] for p in pixels) / len(pixels)
    avg_g = sum(p[1] for p in pixels) / len(pixels)
    avg_b = sum(p[2] for p in pixels) / len(pixels)

    # Normalize to [0, 1] for HSV conversion
    r_norm, g_norm, b_norm = avg_r / 255.0, avg_g / 255.0, avg_b / 255.0
    h, s, v = colorsys.rgb_to_hsv(r_norm, g_norm, b_norm)

    # Boost saturation slightly for vibrant water rendering in VR
    s = min(1.0, s * 1.25)

    # Convert back to RGB
    r_boost, g_boost, b_boost = colorsys.hsv_to_rgb(h, s, v)
    hex_color = f"#{int(r_boost * 255):02X}{int(g_boost * 255):02X}{int(b_boost * 255):02X}"
    return hex_color


@app.route("/getcolor", methods=["GET"])
def get_color():
    """Endpoint queried by Unity AutomaticColorCalibrator.cs"""
    hex_color = sample_screen_color(SAMPLE_X, SAMPLE_Y, BOX_RADIUS)
    print(f"[SERVER] Eyedropper sampled hex color: {hex_color}")
    return Response(hex_color, mimetype="text/plain")


if __name__ == "__main__":
    print("=" * 60)
    print("🌊 VR Shoreline Calibration Server Started")
    print("Ensure reference image is open and visible on screen.")
    print("=" * 60)
    # Listen on all local interfaces on port 8080
    app.run(host="0.0.0.0", port=8080, debug=False)
