import os
from PIL import Image

image_folder = '/home/kevind/Imágenes/'

if __name__ == '__main__':
    for file_name in os.listdir(image_folder):
        name, extension = os.path.splitext(file_name)

        if extension in ['.jpg', '.png', '.jpeg']:
            picture = Image.open(image_folder + file_name)
            picture.save(image_folder + 'compressed_' + file_name, optimize=True, quality=70)
