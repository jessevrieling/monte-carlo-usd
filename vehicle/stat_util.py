import numpy

def randnorm(n, stddev):
	return numpy.random.normal(n, stddev, 1)[0]
