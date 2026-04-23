import imageio.v3 as iio
import numpy as np
import os

os.environ["OPENCV_IO_ENABLE_OPENEXR"] = "1"

#iio.plugins.freeimage.download()

# Create a test image
height, width = 1080, 1920
image = np.random.rand(height, width, 3).astype(np.float32)

# Write EXR file
iio.imwrite("output.exr", image)
print("EXR created with imageio!")

# Read it back to verify
read_image = iio.imread("output.exr")
print(f"Image shape: {read_image.shape}, dtype: {read_image.dtype}")