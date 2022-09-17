import sys
import argparse
import os
import cv2
import shutil
import glob

sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

def main():
    parser = argparse.ArgumentParser(description="PySplitter: Split image into patches for segmentation")

    parser.add_argument("--input-img-suffix", help="Input image suffix", type=str, default="tif")
    parser.add_argument("--input-dir", help="Input dir", type=str, default=None)
    parser.add_argument("--suffix", help="Output format", type=str, default='png')
    parser.add_argument("--target-size", help="Target size", type=int, default=256)
    parser.add_argument("--output-dir", help="Output directory", type=str, default='./output')

    args = parser.parse_args()

    input_img_suffix    = args.input_img_suffix
    input_dir           = args.input_dir
    suffix              = args.suffix
    target_size         = args.target_size
    output_dir          = args.output_dir

    if not os.path.exists(output_dir):
        print("Making directory {}...".format(output_dir))
        os.mkdir(output_dir)

    img_paths = glob.glob(os.path.join(input_dir, "*.{}".format(input_img_suffix)))

    for i, img_path in enumerate(img_paths):
        img_filename = os.path.splitext(os.path.basename(img_path))[0]

        img = cv2.imread(img_path)

        k = 0

        for y in range(0, img.shape[0], target_size):
            for x in range(0, img.shape[1], target_size):
                img_tile = img[y:y + target_size, x:x + target_size]

                if img_tile.shape[0] == target_size and img_tile.shape[1] == target_size:
                    out_img_path = os.path.join(output_dir, "{}_{}.{}".format(img_filename, k, suffix))
                    cv2.imwrite(out_img_path, img_tile)

                k += 1

if __name__ == '__main__':
    main()
