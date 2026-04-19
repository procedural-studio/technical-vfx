import OpenImageIO as oiio
import numpy as np

# Create a simple gradient image (1920x1080, RGB, Float32)
width, height = 1920, 1080
pixels = np.zeros((height, width, 3), dtype=np.float32)

# Create a gradient
for y in range(height):
    for x in range(width):
        pixels[y, x] = [x / width, y / height, 0.5]

# Create ImageSpec
spec = oiio.ImageSpec(width, height, 3, "float")

# Create ImageBuf and set pixels
buf = oiio.ImageBuf(spec)
buf.set_pixels(oiio.ROI(), pixels)

# Write EXR file
buf.write("exr/output_numpy.exr")
print("EXR file created successfully!")