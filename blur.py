import os
from rembg import remove

def remove_background(input_folder, input_filename, output_folder, output_filename):
    # Construct the full path for input and output
    input_path = os.path.join(input_folder, input_filename)
    output_path = os.path.join(output_folder, output_filename)

    with open(input_path, 'rb') as input_file:
        input_data = input_file.read()
        output_data = remove(input_data)

    with open(output_path, 'wb') as output_file:
        output_file.write(output_data)

# Example usage
input_folder = 'C:/Users/KEVIN/Desktop/blur'
input_filename = 'apose_charan_1.jpg'
output_folder = 'C:/Users/KEVIN/Desktop/blur'
output_filename = 'apose_charan_1_remove_background.jpg'

remove_background(input_folder, input_filename, output_folder, output_filename)
