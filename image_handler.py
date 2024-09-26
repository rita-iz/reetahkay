import os
from PIL import Image

class ImageHandler:
    
    def __init__(self, source, destination):
         self.source_folder = source
         self.destination_folder = destination

    def delete_images(self):
        for filename in os.listdir(self.source_folder):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                file_path = os.path.join(self.source_folder, filename)
                os.remove(file_path)
                print(f"Deleted: {file_path}")

    def compress_image(self, image_format: str, quality_level: int,export:bool = True, filename: str=None, verbose: bool=True):
            source_folder = self.source_folder
            destination_folder = self.destination_folder
            if not export:
                destination_folder = source_folder
            i = 0
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            for image in os.listdir(source_folder):
                if not filename:
                    filename = image
                if image.endswith('.jpg') or image.endswith('.jpeg') or image.endswith('.png'):
                    input_path = os.path.join(source_folder, image)
                    base_name, extension = os.path.splitext(image)
                    output_name = f'{base_name}.{image_format}'
                    output_path = os.path.join(destination_folder, output_name)
                    # output_path = os.path.join(destination_folder, f'{filename}-{i}.{image_format}')
                    img = Image.open(input_path)
                    img.save(output_path, image_format, quality=quality_level, optimize=True)
                    i += 1
                    if verbose:
                        print(f'{output_path} Saved')
            print('Done')

source = r'c:\Users\REETAH-KAY\Pictures\PICLAB'
destination = r'c:\Users\REETAH-KAY\Pictures\PICLAB\COMPRESSED'

im = ImageHandler(source, destination)

im.compress_image('webp', 10)