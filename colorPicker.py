# Color Picker from Image Python script that displays an image and allows you to 
# interactively click on it to retrieve the color at the clicked position.

import cv2

image = cv2.imread('IMAGE_PATH.png')  # Replace 'your_image.jpg' with your image file path

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        color = image[y, x]
        print(f"Color at position ({x}, {y}): ({color[0]}, {color[1]}, {color[2]})")

if __name__ == '__main__':
  
    # Create a window and set the mouse callback function
    cv2.imshow('Image', image)
    cv2.setMouseCallback('Image', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
