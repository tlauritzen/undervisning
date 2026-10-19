import os

from exif import Image

for f in os.listdir("images"):
     if f.endswith(".jpg") or f.endswith(".jpeg"):
          my_image = Image("./images/"+f)
          print(my_image.has_exif)
          print(my_image.list_all())
          print(my_image.get("focal_length_in_35mm_film"))
          print(my_image.get("make"))
          print(my_image.get("model"))

# with open('images/DSC07821.jpeg', 'rb') as image_file:
#      my_image = Image(image_file)

