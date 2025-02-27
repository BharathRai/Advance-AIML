import cv2
import numpy as np

# 1. Read the image
img = cv2.imread("image.jpg")
if img is None:
    print("Error: Image not found.")
    exit()

# Function to display image and wait for key press
def show(title, image):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyWindow(title)

# 2. Display Original Image
show("Original Image", img)

# 3. Convert to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
show("Grayscale", gray)

# 4. Apply Binary Threshold
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
show("Binary Threshold", thresh)

# 5. Gaussian Blur
blur = cv2.GaussianBlur(img, (7, 7), 0)
show("Gaussian Blur", blur)

# 6. Canny Edge Detection
edges = cv2.Canny(img, 100, 200)
show("Canny Edges", edges)

# 7. Dilate Edges
dilated = cv2.dilate(edges, None, iterations=1)
show("Dilated Edges", dilated)

# 8. Erode Image
eroded = cv2.erode(dilated, None, iterations=1)
show("Eroded", eroded)

# 9. Resize Image (half the size)
resized = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
show("Resized", resized)

# 10. Rotate Image (45 degrees)
(h, w) = img.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(img, M, (w, h))
show("Rotated", rotated)

# 11. Flip Image Horizontally
flip_h = cv2.flip(img, 1)
show("Flipped Horizontally", flip_h)

# 12. Flip Image Vertically
flip_v = cv2.flip(img, 0)
show("Flipped Vertically", flip_v)

# 13. Draw Text on Image
text_img = img.copy()
cv2.putText(text_img, "OpenCV", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
show("Text Added", text_img)

# 14. Draw a Rectangle
rect_img = img.copy()
cv2.rectangle(rect_img, (50, 50), (200, 200), (255, 0, 0), 2)
show("Rectangle", rect_img)

# 15. Draw a Circle
circle_img = img.copy()
cv2.circle(circle_img, (100, 100), 50, (0, 0, 255), 2)
show("Circle", circle_img)

# 16. Adjust Brightness and Contrast
alpha = 1.5  # Contrast control (1.0-3.0)
beta = 20    # Brightness control (0-100)
adjusted = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
show("Brightness/Contrast Adjusted", adjusted)

# Close all windows
cv2.destroyAllWindows()
