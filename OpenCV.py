import cv2
import numpy as np

# Function to update color range parameters using trackbars
def update_range(val):
    global lower_color, upper_color
    lower_color[0] = cv2.getTrackbarPos("Hue Min", "Result")
    lower_color[1] = cv2.getTrackbarPos("Saturation Min", "Result")
    lower_color[2] = cv2.getTrackbarPos("Value Min", "Result")
    upper_color[0] = cv2.getTrackbarPos("Hue Max", "Result")
    upper_color[1] = cv2.getTrackbarPos("Saturation Max", "Result")
    upper_color[2] = cv2.getTrackbarPos("Value Max", "Result")
    update_result()

# Function to update blur parameters using trackbars
def update_blur(val):
    global blur_kernel_size
    blur_kernel_size = cv2.getTrackbarPos("Kernel Size", "Result")
    update_result()

# Function to update the result image based on the latest parameters
def update_result():
    global result, plant_count
    blurred = cv2.GaussianBlur(img, (blur_kernel_size, blur_kernel_size), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    result = cv2.bitwise_and(img, img, mask=mask)

    # Find contours of plants
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    plant_count = 0
    for cnt in contours:
        # Filter contours by area to exclude small noise
        area = cv2.contourArea(cnt)
        if area > 1000:
            plant_count += 1
            cv2.drawContours(result, [cnt], -1, (0, 255, 0), 2)

    # Update plant count display
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(result, "Plant count: " + str(plant_count), (10, 30), font, 1, (0, 255, 0), 2)

    # Show result image
    cv2.imshow("Result", result)

# Load image
img = cv2.imread("Knipsel.png")

# Initialize color range and blur parameters
lower_color = np.array([40, 40, 40])
upper_color = np.array([70, 255, 255])
blur_kernel_size = 5

# Create trackbars to adjust parameters
cv2.namedWindow("Result",0)
cv2.createTrackbar("Hue Min", "Result", lower_color[0], 180, update_range)
cv2.createTrackbar("Hue Max", "Result", upper_color[0], 180, update_range)
cv2.createTrackbar("Saturation Min", "Result", lower_color[1], 255, update_range)
cv2.createTrackbar("Saturation Max", "Result", upper_color[1], 255, update_range)
cv2.createTrackbar("Value Min", "Result", lower_color[2], 255, update_range)
cv2.createTrackbar("Value Max", "Result", upper_color[2], 255, update_range)
cv2.createTrackbar("Kernel Size", "Result", blur_kernel_size, 50, update_blur)

# Initialize result image and plant count
result = img.copy()
plant_count = 0

# Update result image and plant count
update_result()

# Display original and result images
cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()