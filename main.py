
import cv2
import pytesseract

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Read the image
img = cv2.imread("input.png")

if img is None:
    print("Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Reduce noise
    blur = cv2.GaussianBlur(gray, (3, 3), 0)

    # Convert to black and white
    _, binary = cv2.threshold(
        blur, 0, 255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    # Extract text
    text = pytesseract.image_to_string(binary)

    # Display output
    print("Recognized Text:")
    print(text)

    # Show processed image
    cv2.imshow("Processed Image", binary)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
