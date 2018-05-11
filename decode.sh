#!/bin/sh

# EMNIST Balanced:	131,600 characters. 47 balanced classes.
python decode.py gzip/emnist-balanced-train-images-idx3-ubyte gzip/emnist-balanced-train-labels-idx1-ubyte gzip/emnist-balanced-mapping.txt ./emnist_balanced/train
python decode.py gzip/emnist-balanced-test-images-idx3-ubyte gzip/emnist-balanced-test-labels-idx1-ubyte gzip/emnist-balanced-mapping.txt ./emnist_balanced/test

# EMNIST ByClass:		814,255 characters. 62 unbalanced classes.
python decode.py gzip/emnist-byclass-train-images-idx3-ubyte gzip/emnist-byclass-train-labels-idx1-ubyte gzip/emnist-byclass-mapping.txt ./emnist_byclass/train
python decode.py gzip/emnist-byclass-test-images-idx3-ubyte gzip/emnist-byclass-test-labels-idx1-ubyte gzip/emnist-byclass-mapping.txt ./emnist_byclass/test

# EMNIST ByMerge: 	814,255 characters. 47 unbalanced classes.
python decode.py gzip/emnist-bymerge-train-images-idx3-ubyte gzip/emnist-bymerge-train-labels-idx1-ubyte gzip/emnist-bymerge-mapping.txt ./emnist_bymerge/train
python decode.py gzip/emnist-bymerge-test-images-idx3-ubyte gzip/emnist-bymerge-test-labels-idx1-ubyte gzip/emnist-bymerge-mapping.txt ./emnist_bymerge/test

# EMNIST Digits:		280,000 characters. 10 balanced classes.
python decode.py gzip/emnist-digits-train-images-idx3-ubyte gzip/emnist-digits-train-labels-idx1-ubyte gzip/emnist-digits-mapping.txt ./emnist_digits/train
python decode.py gzip/emnist-digits-test-images-idx3-ubyte gzip/emnist-digits-test-labels-idx1-ubyte gzip/emnist-digits-mapping.txt ./emnist_digits/test

# EMNIST Letters:		145,600 characters. 26 balanced classes.
python decode.py gzip/emnist-letters-train-images-idx3-ubyte gzip/emnist-letters-train-labels-idx1-ubyte gzip/emnist-letters-mapping.txt ./emnist_letters/train
python decode.py gzip/emnist-letters-test-images-idx3-ubyte gzip/emnist-letters-test-labels-idx1-ubyte gzip/emnist-letters-mapping.txt ./emnist_letters/test
