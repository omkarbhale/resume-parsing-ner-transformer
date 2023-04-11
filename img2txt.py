import os
import cv2
import pytesseract

def image_to_text(image_path):
    """
    Converts an image to text using pytesseract OCR.

    Args:
        image_path (str): Path to the image file.

    Returns:
        str: The text extracted from the image.
    """
    # Load the image using OpenCV
    img = cv2.imread(image_path)

    # Preprocess the image (optional)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(img, 3)

    # Perform OCR using pytesseract
    text = pytesseract.image_to_string(img)

    # Return the text
    return text

def batch_image_to_text(input_dir, output_dir):
    """
    Converts a batch of images to text using the image_to_text function.
    Loops over all image files in input_dir and saves the output to text files
    in output_dir with the same filename.

    Args:
        input_dir (str): Path to the input directory containing image files.
        output_dir (str): Path to the output directory to save text files.
    """
    # Loop over all image files in input_dir
    for filename in os.listdir(input_dir):
        if filename.endswith(".jpg"):
            image_path = os.path.join(input_dir, filename)

            # Convert the image to text using the image_to_text function
            text = image_to_text(image_path)

            # Write the text to a file in output_dir with the same filename
            text_filename = os.path.splitext(filename)[0] + ".txt"
            text_path = os.path.join(output_dir, text_filename)
            with open(text_path, "w") as text_file:
                text_file.write(text)
                print(f"{text_path}")

if __name__ == "__main__":
    input_dir = "./resumes"
    output_dir = "./resumes_text"
    batch_image_to_text(input_dir, output_dir)