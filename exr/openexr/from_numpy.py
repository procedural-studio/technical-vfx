import OpenEXR
import Imath
import numpy as np

def create_exr_low_level(output_path, width=1920, height=1080):
    # Create test data
    r = np.random.rand(height, width).astype(np.float32)
    g = np.random.rand(height, width).astype(np.float32)
    b = np.random.rand(height, width).astype(np.float32)
    
    # Create header
    header = OpenEXR.Header(width, height)

    header["channels"] = OpenEXR.ChannelList(
        {"R": Imath.Channel(Imath.PixelType(1)),
         "G": Imath.Channel(Imath.PixelType(1)),
         "B": Imath.Channel(Imath.PixelType(1))}
    )

    '''
        channels = OpenEXR.ChannelList()       ^^^^^^^^^^^^^^^^^^^
        AttributeError: module 'OpenEXR' has no attribute 'ChannelList'
    '''
    
    # Write EXR
    exr_file = OpenEXR.OutputFile(output_path, header)
    exr_file.writePixels({"R": r.tobytes(), "G": g.tobytes(), "B": b.tobytes()})
    exr_file.close()
    
    print(f"Created {output_path} with low-level OpenEXR")

create_exr_low_level("lowlevel.exr")