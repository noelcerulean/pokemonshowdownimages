from PIL import Image
im = Image.open(r"pokemonicons-sheet.png")
val = input("> ")
val = int(val)
row = val // 12
col = val % 12
width = 40
height = 30
left = col * width
top = row * height
right = left + width
bottom = top + height

im1 = im.crop((left, top, right, bottom))
 
im1.show()