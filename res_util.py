import numpy as np

def vdivout(vin, r1, r2):
	return r2 / (r1 + r2) * vin

def stddevr(r, tolerance):
	return (tolerance / 100 * r) / (3 / 5 * tolerance)

def randrnorm(r, stddev):
	return np.random.normal(loc=r, scale=stddev, size=1)[0]
