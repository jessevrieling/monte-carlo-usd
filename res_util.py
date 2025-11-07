import numpy as np

def vdivout(vin, r1, r2):
	return r2 / (r1 + r2) * vin

def randrnorm(r, stddev):
	return np.random.normal(loc=r, scale=stddev, size=1)[0]
