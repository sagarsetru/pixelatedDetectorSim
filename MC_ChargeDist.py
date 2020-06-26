#Classes for Monte Carlo simulation for finding charge distribution on Anode with pads of variable size
#to determine resolution for varying pad sizes
#assume fixed charge cloud diameter
#DIAMETER = 3.5 mm
#(space between anode and MCP: 2.5 mm)


class ChargeCloudGaussian:
	"""class to make Gaussian charge cloud"""
	"""6*sigma=3.5 mm"""
	"""therefore, sigma = 0.5833 mm"""
        def __init__(self,sigma=0.5833):
                self.sigma = sigma
	#...

        def gausscloud(self,x,y):
	"""returns a symmetric 2d gaussian profile on the x,y grid, center = 0"""
                return 1./(self.sigma*np.sqrt(2.*pi))*np.exp(-((x**2.)/(2.*self.sigma**2.)+(y**2.)/(2.*self.sigma**2.)))
	#...
	
        def __call__(self):
	"""returns a symmetric 2d Gaussian profile
	centered in the middle of x by y array.
	Gaussian evaluated in 0.01 increments from -2 to 2
	in both axes."""
                # x,y = np.mgrid[0:20,0:20]
				# x = np.linspace(-6000,6000,0.01)
				# y = np.linspace(-6000,6000,0.01)
				x = np.arange(-40,41,0.01)
				y = np.arange(-40,41,0.01)
				return self.gausscloud(x,y)
	#...
#...

class CloudOnPad:
        """class to determine distribution of charge on one pad"""
		"""pad boundary determined by x1, x2, y1, y2"""
        def __init__(self,x1,x2,y1,y2,gauss,flat):
                self.x1=x1
                self.y1=y1
                self.x2=x2
                self.y2=y2
                self.gauss=gauss
                self.flat=flat
	#...
        def __call__(self,x1,x2,y1,y2):
        """generates an array, each of whose entry stands for one pad,
        each of whose elements store the fraction of total charge in that pad"""
                if gauss=1:
                        gaussiancloud = ChargeCloudGaussian()
                        return dblquad(lambda x, y: gaussiancloud, x1,x2, lambda x: y1,lambda x: y2)
						#integrates 2d Gaussian according to bounds x1,x2 and y1,y2
                elif flat=1:
                        flatcloud = ChargeCloudFlat()
                        return dblquad(lambda x, y: flatcloud,x1,x2,lambda x: y1,lambda x: y2)
						#integrates flat cloud according to bounds x1,x2 and y1,y2
                else:
                        raise ValueError("Charge cloud type not specified.")
	#...
#...

####################################
class ChargeCloudFlat:
	"""class to make uniform, flat, circular charge cloud"""
        def __init__(self,radius=1.75):
                self.radius=radius
	# ...
        def flatcloud(self,x,y):
	"""returns a flat, circular profile on the x, y grid"""
                if x**2 + y**2 <= radius**2:
                        return 1
                else:
                        return 0
	#...
        def __call__(self):
	"""returns a flat distribution centered in middle
	of x by y array"""
                # x,y = mp.mgrid[0:20,0:20]
				# x = np.linspace(-6000,6000,0.01)
				# y = np.linspace(-6000,6000,0.01)
				x = np.arange(-40,41,0.01)
				y = np.arange(-40,41,0.01)				
				return self.flatcloud(x,y)
	#...
#...

# class AnodePadsX:
	# """class that returns an array of the x coordinates of anode pads with given length"""
        # def __init__(self,length):
                # self.length=length #length of each pad
	# #...
		# def __call__(self,length):
			# """returns anode pad as an array of coordinates
			# for the boundary of each pad along X."""
					# #x1=np.linspace(-5,5,1)
					# #x1 = range(-5,6)
					# #xcoord = [i * length for i in x1]
					# xcoord = np.arange(-35,36,length)
					# return xcoord
	# #...
# #...
# class AnodePadsY:
	# """class that returns array of y coordinates of anode pads with given width"""
        # def __init__(self,width):
                # self.width=width #width of each pad
	# #...
		# def __call__(self,width):
			# """returns anode pad as an array of coordinates
			# for the boundary of each pad along Y."""
					# #y1=np.linspace(-5,5,1)
					# #y1 = range(-5,6)
					# #ycoord = [i * width for i in y1]
					# ycoord = np.arange(-35,36,width)
					# return ycoord
	# #...
# #...