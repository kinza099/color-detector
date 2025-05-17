import cv2
import pandas as pd

# Constants and initialization
IMAGE_PATH = 'image.png'
COLOR_CSV_PATH = 'colors.csv'
COLUMN_NAMES = ["Color", "Name", "Hex", "R", "G", "B"]

# Load image and color data
image = cv2.imread(IMAGE_PATH)
color_data = pd.read_csv(COLOR_CSV_PATH, names=COLUMN_NAMES, header=None)

# Global variables
is_clicked = False
selected_rgb = (0, 0, 0)
mouse_x = mouse_y = 0

def find_closest_color_name(R, G, B):
    """Find the closest color name from the dataset."""
    min_distance = float('inf')
    closest_name = ""
    for i in range(len(color_data)):
        current = color_data.loc[i]
        distance = abs(R - int(current["R"])) + abs(G - int(current["G"])) + abs(B - int(current["B"]))
        if distance < min_distance:
            min_distance = distance
            closest_name = current["Name"]
    return closest_name

def handle_mouse_event(event, x, y, flags, param):
    """Mouse callback function."""
    global is_clicked, selected_rgb, mouse_x, mouse_y
    if event == cv2.EVENT_LBUTTONDBLCLK:
        mouse_x, mouse_y = x, y
        b, g, r = image[y, x]
        selected_rgb = (int(r), int(g), int(b))
        is_clicked = True

# Setup display window and mouse callback
cv2.namedWindow('Color Detector')
cv2.setMouseCallback('Color Detector', handle_mouse_event)

while True:
    temp_image = image.copy()
    if is_clicked:
        r, g, b = selected_rgb
        color_name = find_closest_color_name(r, g, b)
        color_text = f"{color_name}  R={r} G={g} B={b}"

        # Display colored rectangle with text
        cv2.rectangle(temp_image, (20, 20), (750, 60), (b, g, r), -1)
        text_color = (0, 0, 0) if r + g + b >= 600 else (255, 255, 255)
        cv2.putText(temp_image, color_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, text_color, 2, cv2.LINE_AA)

    # Show the result
    cv2.imshow("Color Detector", temp_image)

    # Exit on 'Esc' key
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
