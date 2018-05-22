import os
import argparse
import bitstring
import numpy as np
from PIL import Image, ImageEnhance

parser = argparse.ArgumentParser()
parser.add_argument('images_binfile')
parser.add_argument('labels_binfile')
parser.add_argument('mapping_txtfile')
parser.add_argument('output_dir')
parser.add_argument('--brightness', type=float, default=1.0)
parser.add_argument('--sharpness', type=float, default=2.0)
parser.add_argument('--contrast', type=float, default=3.0)

def main(args):

    args.images_binfile = os.path.expanduser(args.images_binfile)
    args.labels_binfile = os.path.expanduser(args.labels_binfile)
    args.mapping_txtfile = os.path.expanduser(args.mapping_txtfile)
    args.output_dir = os.path.expanduser(args.output_dir)

    # create output root directory (if necessary)
    if os.path.exists(args.output_dir) == False:
        os.makedirs(args.output_dir)

    # create mapping list
    with open(args.mapping_txtfile, 'r') as f:
        lines = f.readlines()
        label_map = {}
        for line in lines:
            class_id = int(line.split(' ')[0])
            character = chr(int(line.split(' ')[1]))
            label_map[class_id] = character

    # read images binfile header
    images_bitstream = bitstring.ConstBitStream(filename=args.images_binfile)
    images_bitstream.read('int:32') # magic
    n_images = images_bitstream.read('int:32')
    img_width = images_bitstream.read('int:32')
    img_height = images_bitstream.read('int:32')

    # read labels binfile header
    labels_bitstream = bitstring.ConstBitStream(filename=args.labels_binfile)
    labels_bitstream.read('int:32') # magic
    n_labels = labels_bitstream.read('int:32')

    # validation
    assert n_images == n_labels, 'the number of images is not the same as that of images.'
    n_samples = n_images

    cnt = 0
    for i in range(n_samples):
        cnt += 1

        # read a single label record
        record_label = labels_bitstream.read('uint:8')
        # reconstruct the label id
        label = np.uint8(record_label)
        # decoded label character
        character = label_map[label]

        # create subdirectory (if necessary)
        subdir = os.path.join(args.output_dir, character)
        if os.path.exists(subdir) == False:
            os.makedirs(subdir)

        # read a single image record
        record_image = images_bitstream.readlist('%d*uint:8' % (img_width*img_height))
        # reconstruct the image data
        pixel_data = np.array(record_image, dtype=np.uint8).reshape(img_height, img_width)
        pixel_data = pixel_data.T
        image = Image.fromarray(pixel_data)

        # apply enhancements
        # brightness
        if args.brightness != 1.0:
            image = ImageEnhance.Brightness(image).enhance(args.brightness)
        # sharpness
        if args.sharpness != 1.0:
            image = ImageEnhance.Sharpness(image).enhance(args.sharpness)
        # contrast
        if args.contrast != 1.0:
            image = ImageEnhance.Contrast(image).enhance(args.contrast)

        # save image
        fname = os.path.join(subdir, '%d.png' % cnt)
        image.save(fname)
        print('(%d/%d) decoded image was saved as %s' % (i+1, n_samples, fname))

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
