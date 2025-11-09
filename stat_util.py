import numpy as np

def stddevr(r, tolerance):
	return tolerance / 100 * r / 3

def randrnorm(r, stddev):
	return np.random.normal(loc=r, scale=stddev, size=1)[0]

def cp(lsl, usl, stddev):
	return (usl - lsl) / (6 * stddev)
