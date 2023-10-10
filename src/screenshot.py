# screenshot.py
import pyautogui
from PIL import Image


def capture_screenshot():
    """Capture a screenshot of the entire screen, crop out the menu bar and dock, and keep only the middle half horizontally."""
    screenshot = pyautogui.screenshot()

    # Define the dimensions for cropping
    # (left, upper, right, lower)

    # Determine the horizontal boundaries for the middle half
    horizontal_start = screenshot.width * 0.25  # Start at 25% of the width
    horizontal_end = screenshot.width * 0.75  # End at 75% of the width

    # These values depend on your screen resolution and the size of the menu bar and dock.
    # Adjust them as needed.
    crop_dimensions = (
    horizontal_start, 30, horizontal_end, screenshot.height - 50)  # example values for vertical cropping
    cropped_screenshot = screenshot.crop(crop_dimensions)

    return cropped_screenshot
