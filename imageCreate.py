import array
width,height = 128,64

PPMheader = 'P6\n' +str(width) + ' ' +str(height) + '\n255\n'

# Create and fill a red PPM image
image = array.array('B', [255, 0, 0] * width * height)

# Save as PPM image
with open('result.ppm', 'wb') as f:
   f.write(bytearray(PPMheader, 'ascii'))
   image.tofile(f)