import imageio.v3 as iio
import numpy as np

def convert_with_imageio(input_path, output_path):
    # Read input image
    img = iio.imread(input_path)
    
    # Convert to float32 and normalize to 0-1
    if img.dtype != np.float32:
        img = img.astype(np.float32) / 255.0
    
    # Write as EXR
    iio.imwrite(output_path, img, plugin="opencv")
    print(f"Converted {input_path} to {output_path}")

convert_with_imageio("exr/imageio/input.jpg", "exr/imageio/output_png.exr")