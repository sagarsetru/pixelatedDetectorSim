### Python script that takes two images and returns the element-wise ratio of them

## if checkSameVals == 1, then will save as a separate textfile those values which were the same in each matrix
checkSameVals = 0

### author: Sagar Setru

import sys, os, getopt
import numpy as np


myopts, args = getopt.getopt(sys.argv[1:],"a:b:o:h")
for o, a in myopts:
    if o == '-a':
        infile1=a
    elif o == '-b':
        infile2=a
    elif o == '-o':
        outfile=a
    elif o == '-h':
        print 'Usage:'
        print "-a <inputImage1_Numerator.txt> -b <inputImage2_Denominator -o <outputImageRatio.txt>"
        sys.exit()


imageNumerator = np.loadtxt(infile1)
imageDenominator  = np.loadtxt(infile2)

im_ratio = np.divide(imageNumerator,imageDenominator)

np.savetxt(outfile,im_ratio)

if checkSameVals == 1:
    indices = np.where(im_ratio==1)
    sameVals = imageNumerator[indices]
    np.savetxt("overlappingFigureValues.txt",sameVals)
    np.savetxt("indicesOverlappingFigureValues.txt",indices)

