import mss
from PIL import Image

def capture_screenshot(monitor_index=0):
    with mss.mss() as sct:
        monitor = sct.monitors[monitor_index]
        screen_capture = sct.grab(monitor)
        screenshot_image = Image.frombytes('RGB', screen_capture.size, screen_capture.bgra, 'raw', 'BGRX')
        return screenshot_image