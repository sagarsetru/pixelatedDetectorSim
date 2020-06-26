from MC_ChargeDist.py import CloudOnPad

import pyfits
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D

import os
import datetime

from scipy import linspace
from scipy import pi,sqrt,exp
from scipy.integrate import quad,dblquad

from MC_ChargeDist.py import CloudOnPad

"""initialize pad dimensions and MC loop length"""
# length = 5
# width = 5
padsize = 2
#size of pads in mm
#loopsize = 1000

"""create directory for saving txt files"""
# date = datetime.date.today().strftime("%m_%d_%Y")
#path = "C:\Users\Sagar\Documents\Documents\argonne\MCChargeDist\"+date
#^^^^directory for Sagar's laptop
# path = "/users/detector/ssetru/mcp_testing/charge_pad_simulation/"+date
# if not os.path.exists(path):
	# os.makedirs(path)
	
"""Run MC loop"""

# """loop over different padsizes"""
# for j in range(0,padsize.size)
	# """create filename for saving eventual pad charge distribution matrix"""
	# fileName = 'ChargeDist_padsize_'+str(length)+'_x_'+str(width)+'_mm'
	# completeFileName = os.path.join(path, fileName)
	
	"""Monte Carlo--position charge cloud randomly over pads"""
	# for t in range(0,loopsize):
		"""create anode pad coordinates"""
		# length = padsize[j]
		# width = padsize[j]
		# xpads = AnodePadsX(padsize)
		# ypads = AnodePadsY(padsize)
		xpads = np.arange(-35,36,padsize)
		ypads = np.arange(-35,36,padsize)
		
		"""set random offset"""
		xoffset = np.random.random()
		xoffset = xoffset * length
		yoffset = np.random.random()
		yoffset = yoffset * width
		
		"""add offsets to coordinates of pads (to shift pads relative to charge cloud)"""
		xpads2 = [i + xoffset for i in xpads]
		ypads2 = [i + yoffset for i in ypads]
		
		"""3D array. each entry represents a pad. each square slice represents one entire cloud-on-pads
		simulation."""
		padcharge0 = np.zeros((xpads.size-1,ypads.size-1))
		padcharge = np.zeros((xpads2.size-1,ypads2.size-1))
		
		"""loop over each pad's coordinates, integrate under charge cloud,
		add charge to padcharge matrix"""
		for q in range(1,xpads2.size):
			for h in range(1,ypads2.size):
				x1 = xpads2[q]
				x2 = xpads2[q+1]
				y1 = ypads2[h]
				y2 = ypads2[h+1]
				padcharge[q,h] = CloudOnPad(x1,x2,y1,y2,gauss=1)
			#...
		#...
		for q in range(1,xpads2.size):
			for h in range(1,ypads2.size):
				x1 = xpads[q]
				x2 = xpads[q+1]
				y1 = ypads[h]
				y2 = ypads[h+1]
				padcharge0[q,h] = CloudOnPad(x1,x2,y1,y2,gauss=1)
			#...
		#...
		
	#...
	
	"""save padcharge matrix as a txt file in a dated directory"""
	# np.savetxt(completeFileName,padcharge,delimiter=' ')