# EMNIST

## About this repository

This repository provide you python scripts for decoding images
of the [EMNSIT](https://www.nist.gov/itl/iad/image-group/emnist-dataset) from the official binary format files.
The EMNIST contains not only digits images but also alphabet ones.

## How to use our scripts

### 1. Download the official binary format files and extract them.

```bash
$ sh download_binary.sh
$ unzip gzip.zip
$ cd gzip/
$ gzip -d emnist-*.gz
```

### 2. Choose a desired dataset

The EMNIST dataset consists of some datasets.  
Choose desired one from the following list.  

1. `EMNIST Balanced`:	131,600 characters. 47 balanced classes.
2. `EMNIST ByClass`:		814,255 characters. 62 unbalanced classes.
3. `EMNIST ByMerge`: 	814,255 characters. 47 unbalanced classes.
4. `EMNIST Digits`:		280,000 characters. 10 balanced classes.
5. `EMNIST Letters`:		145,600 characters. 26 balanced classes.

### 3. Decode images

Here I'll show an example in the case of `EMNIST Balanced` (whatever you choose, the following process is exactly the same).  

First, comment out the other lines than the part of `EMNIST Balanced` from `decode.py` as follows.

```bash
#!/bin/sh

# EMNIST Balanced:	131,600 characters. 47 balanced classes.
python decode.py gzip/emnist-balanced-train-images-idx3-ubyte gzip/emnist-balanced-train-labels-idx1-ubyte gzip/emnist-balanced-mapping.txt ./emnist_balanced/train
python decode.py gzip/emnist-balanced-test-images-idx3-ubyte gzip/emnist-balanced-test-labels-idx1-ubyte gzip/emnist-balanced-mapping.txt ./emnist_balanced/test

# EMNIST ByClass:		814,255 characters. 62 unbalanced classes.
#python decode.py gzip/emnist-byclass-train-images-idx3-ubyte gzip/emnist-byclass-train-labels-idx1-ubyte gzip/emnist-byclass-mapping.txt ./emnist_byclass/train
#python decode.py gzip/emnist-byclass-test-images-idx3-ubyte gzip/emnist-byclass-test-labels-idx1-ubyte gzip/emnist-byclass-mapping.txt ./emnist_byclass/test

# EMNIST ByMerge: 	814,255 characters. 47 unbalanced classes.
#python decode.py gzip/emnist-bymerge-train-images-idx3-ubyte gzip/emnist-bymerge-train-labels-idx1-ubyte gzip/emnist-bymerge-mapping.txt ./emnist_bymerge/train
#python decode.py gzip/emnist-bymerge-test-images-idx3-ubyte gzip/emnist-bymerge-test-labels-idx1-ubyte gzip/emnist-bymerge-mapping.txt ./emnist_bymerge/test

# EMNIST Digits:		280,000 characters. 10 balanced classes.
#python decode.py gzip/emnist-digits-train-images-idx3-ubyte gzip/emnist-digits-train-labels-idx1-ubyte gzip/emnist-digits-mapping.txt ./emnist_digits/train
#python decode.py gzip/emnist-digits-test-images-idx3-ubyte gzip/emnist-digits-test-labels-idx1-ubyte gzip/emnist-digits-mapping.txt ./emnist_digits/test

# EMNIST Letters:		145,600 characters. 26 balanced classes.
#python decode.py gzip/emnist-letters-train-images-idx3-ubyte gzip/emnist-letters-train-labels-idx1-ubyte gzip/emnist-letters-mapping.txt ./emnist_letters/train
#python decode.py gzip/emnist-letters-test-images-idx3-ubyte gzip/emnist-letters-test-labels-idx1-ubyte gzip/emnist-letters-mapping.txt ./emnist_letters/test
```

Second, run `decode.sh` in your command line.

```bash
$ sh decode.sh
```

After running `decode.sh`, A directory `emnist_balanced` is created in the current directory.  
The training images are saved in `emnist_balanced/train`, while the validation images are in `emnist_balanced/test`.  
