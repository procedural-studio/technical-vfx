from PIL import Image
import OpenImageIO as oiio
import numpy as np

def pil_to_exr(input_path, output_path):
    # Open with PIL
    pil_img = Image.open(input_path).convert("RGB")
    
    # Convert to numpy array
    np_img = np.array(pil_img).astype(np.float32) / 255.0
    
    # Create OIIO buffer
    height, width = np_img.shape[:2]
    channels = np_img.shape[2] if len(np_img.shape) > 2 else 1
    
    spec = oiio.ImageSpec(width, height, channels, "float")
    buf = oiio.ImageBuf(spec)
    buf.set_pixels(oiio.ROI(), np_img)
    
    # Write EXR
    buf.write(output_path)
    print(f"Converted PIL image to {output_path}")


pil_to_exr("exr/openimageio/input.jpg", "exr/openimageio/output_pil.exr")
