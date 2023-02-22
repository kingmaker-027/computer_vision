from PIL import Image
import os

# set paths for input and output folders
input_folder = "resize\image_in"
output_folder = "resize\image_out"

# create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through all files in input folder
for filename in os.listdir(input_folder):
    # get full path of input file
    input_path = os.path.join(input_folder, filename)
    
    # check if file is an image
    if not os.path.isfile(input_path) or not filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
        continue
    
    # open image using Pillow
    with Image.open(input_path) as img:
        # resize image to 640x800 while maintaining aspect ratio
        img = img.resize((640, 800))
        
        # get full path of output file
        output_path = os.path.join(output_folder, filename)
        
        # save resized image to output folder
        img.save(output_path)
