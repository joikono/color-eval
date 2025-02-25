from PIL import Image
import numpy as np
from skimage import color

def get_color_rgb(image_file):
    image = Image.open(image_file).convert("RGB")  # Ensure it's in RGB mode
    image = image.resize((1, 1))  # Resize to 1x1 to get the average color
    rgb = np.array(image).flatten()  # Get RGB values
    return rgb

def get_color_lab(image_file):
    rgb = get_color_rgb(image_file)  # Get the RGB values
    rgb_normalized = rgb / 255.0  # Normalize RGB values to [0, 1]
    lab = color.rgb2lab(rgb_normalized.reshape(1, 1, 3))  # Convert to Lab
    return lab[0][0]  # Return the Lab values as a flat array

def calculate_color_accuracy(target_image, input_image):
    target_lab = get_color_lab(target_image)  # Get Lab values for target image
    input_lab = get_color_lab(input_image)  # Get Lab values for input image

    # Calculate the Euclidean distance in Lab space
    difference = np.sqrt(np.sum((target_lab - input_lab) ** 2))

    # Max distance in Lab space (approximately 100 for CIE76)
    max_distance = np.sqrt(3 * (100 ** 2))  
    normalized_difference = difference / max_distance

    # Convert to accuracy percentage
    accuracy = (1 - normalized_difference) * 100

    return max(0, min(100, accuracy)), target_lab, input_lab
