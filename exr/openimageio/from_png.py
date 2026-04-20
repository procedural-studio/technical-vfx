import OpenImageIO as oiio

def convert_to_exr(input_path, output_path):
    # Read the input image
    in_buf = oiio.ImageBuf(input_path)
    
    # Convert to float32 (EXR standard)
    if in_buf.spec().format.basetype != "float":
        # Normalize 8-bit to 0-1 float range
        in_buf = oiio.ImageBufAlgo.colorconvert(in_buf, "linear", "linear", True)
    
    # Write as EXR
    success = in_buf.write(output_path)
    
    if success:
        print(f"Converted {input_path} to {output_path}")
    else:
        print("Conversion failed!")

# Usage
convert_to_exr("exr/openimageio/input.jpg", "exr/openimageio/output_png.exr")