from PIL import Image
import os
import threading
from tqdm import tqdm

input_dir = "./images_input"
output_dir = "./images_converted"
threads = []

image_extensions = [
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".bmp",
    ".svg",
    ".webp",
    ".tiff",
    ".ico",
    ".jfif",
    ".jpe",
    ".ppm",
    ".pgm",
    ".pbm",
    ".pnm",
    ".heif",
    ".bat",
    ".bpg",
    ".brk"
]

# Choose the target extension
target_extension = ".webp"

# Lower value means lower quality and smaller file size
compression_quality = 60

def process_image(file_name, pbar):
    input_file_path = os.path.join(input_dir, file_name)
    output_file_path = os.path.join(output_dir, os.path.splitext(file_name)[0] + target_extension)
    try:
        with Image.open(input_file_path) as img:
            # Choose the compression quality
            img.save(output_file_path, 'webp', quality=compression_quality)
            pbar.update(1)
            print(f"\x1b[1m\x1b[36m{file_name} converted\x1b[0m")
    except Exception as e:
        print(f"\x1b[31mFailed to convert {file_name}. Error: {e}\x1b[0m")
        pbar.update(1)

input_files = os.listdir(input_dir)

with tqdm(total=len(input_files)) as pbar:
    for file_name in input_files:
        if file_name.lower().endswith(tuple(image_extensions)):
            t = threading.Thread(target=process_image, args=(file_name, pbar))
            threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

print("\033[1;32;40mAll images converted successfully!\033[0m")