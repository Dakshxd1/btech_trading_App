import cv2

# Open the default camera (usually the first one)
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Error: Could not open video device.")
    exit()

# Set frame width and height
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Failed to capture image.")
        break
    
    # 1. Convert the captured frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 2. Apply Gaussian blur to the grayscale image
    blur_frame = cv2.GaussianBlur(gray_frame, (15, 15), 0)
    
    # 3. Apply Canny edge detection
    edges_frame = cv2.Canny(blur_frame, 50, 150)
    
    # 4. Apply binary thresholding
    _, thresh_frame = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_BINARY)
    
    # Display the original and processed frames
    cv2.imshow('Original', frame)
    cv2.imshow('Grayscale', gray_frame)
    cv2.imshow('Blurred', blur_frame)
    cv2.imshow('Edges', edges_frame)
    cv2.imshow('Thresholded', thresh_frame)
    
    # Break the loop if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()