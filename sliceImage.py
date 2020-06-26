### Python code that slices an image matrix
### Author Sagar Setru

import sys, os, getopt
import numpy as np

myopts, args = getopt.getopt(sys.argv[1:],"i:o:h")
for o, a in myopts:
    if o == '-i':
        infile=a
    elif o == '-o':
        outfile=a
    elif o == '-h':
        print 'Usage:'
        print "-i <inputImage.txt> -o <outputSlicedImage.txt>"
        sys.exit()

## Ranges give to my by Jun
# [427:2689,813:3066]

im_orig = np.loadtxt(infile)

im_sliced = im_orig[427:2689,813:3066]

np.savetxt(outfile,im_sliced)
