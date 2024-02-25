import os
import cv2

# Directory containing the images
images_directory = 'images'

# Check if the directory exists
if not os.path.exists(images_directory):
    print(f"Error: Directory '{images_directory}' not found.")
    exit()

# List all files in the directory
image_files = os.listdir(images_directory)

# Loop through each image file
for image_file in image_files:
    # Check if the file is an image file
    if image_file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        # Construct the path to the image
        image_path = os.path.join(images_directory, image_file)
        
        # Load the image
        image = cv2.imread(image_path)
        
        # Check if the image is loaded successfully
        if image is not None:
            # Display the image in a window with the filename as the window title
            cv2.imshow(image_file, image)
            print(f"Image '{image_file}' loaded successfully.")
        else:
            print(f"Error: Failed to load image '{image_file}'.")

# Wait for a key press to close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
