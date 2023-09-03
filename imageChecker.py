import os
import shutil
import cv2

# Defined list of positions (using Picker)

positions_to_check = [
  {'position': (318, 235), 'color': (209, 227, 188)},
  {'position': (411, 196), 'color': (196, 248, 230)},
  {'position': (382, 229), 'color': (225, 226, 186)},
]

if __name__ == '__main__':
  
    # Create a list of image file paths
    input_image_folder = 'dataset'
    output_folder = 'output'
  
      # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
      
    image_files = [os.path.join(input_image_folder, filename) for filename in os.listdir(image_folder) if
                   filename.endswith(('.jpg', '.png'))]

    # Iterate through the image files
    for image_file in image_files:
        # Load the image
        img = cv2.imread(image_file)

        # Initialize a variable to keep track of whether all positions are found
        all_positions_found = True

        # Check if all positions exist on the image with the specified colors
        for pos_info in positions_to_check:
            position = pos_info['position']
            color = pos_info['color']

            # Extract the color at the specified position
            pixel_color = img[position[1], position[0]]

            # Check if the extracted color matches the specified color
            if not all([pixel_color[i] == color[i] for i in range(3)]):
                all_positions_found = False
                break

        # If all positions are found, move the image to the output folder
        if all_positions_found:
            filename = os.path.basename(image_file)
            output_path = os.path.join(output_folder, filename)
            shutil.move(image_file, output_path)
            print(f"Moved {filename} to {output_path}")
