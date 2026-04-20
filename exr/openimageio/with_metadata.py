import OpenImageIO as oiio
import numpy as np

def create_exr_with_metadata():
    width, height = 1920, 1080
    pixels = np.random.rand(height, width, 3).astype(np.float32)
    
    spec = oiio.ImageSpec(width, height, 3, "float")
    
    # Add custom metadata
    spec.attribute("artist", "Your Name")
    spec.attribute("software", "Python + OpenImageIO")
    spec.attribute("EXR:compression", "ZIP")  # ZIP, PIZ, DWAA, etc.
    spec.attribute("comment", "Test EXR file")
    
    buf = oiio.ImageBuf(spec)
    buf.set_pixels(oiio.ROI(), pixels)
    buf.write("exr/openimageiometadata.exr")

create_exr_with_metadata()