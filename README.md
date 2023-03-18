# Convert and Compress Images

This script converts image files in a specified input directory to the WebP format with the specified compression quality.
It uses the Python Imaging Library (PIL) to handle image processing and threading to speed up the conversion process.

### Dependencies:

- `Python 3.x`
- `PIL`
- `tqdm`

### Running Script

Run `python convert.py` in the root dir

The images to be converted should be placed in the `/assets_raw` directory and the converted images will be saved in the `/assets_converted` directory. The compression quality can be set by changing the value of the `compression_quality` variable and additional extensions can be added to the `image_extensions` list.

### WIP

- Add input for quality, target extension and relevant dir
