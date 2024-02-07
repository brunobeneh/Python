# The PIL (Pillow library) it's a library to work with images and have a lot of functionalities.

from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

# We can blur the image:

# filtered_img = img.filter(ImageFilter.SMOOTH)

# We can convert the image as well. The 'L' is for Grey Scale:

filtered_img = img.convert('L')

# We can show (open) the image:

# filtered_img.show()

# Rotate the image:

crooked = filtered_img.rotate(90)

# We can modify our image with this func: .thumbanail((size, size))

# Ex: img.thumbnail((400, 200))

# We can save our image with the filter:

# filtered_img.save("grey_pikachu.png", 'png')

crooked.save("crooked_pikachu.png", 'png')