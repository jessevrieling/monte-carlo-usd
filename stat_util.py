import numpy as np

def stddevr(r, tolerance):
	return tolerance / 100 * r / 3

def percstddev(r, stddevr):
	return 300 * stddevr / r

def randrnorm(r, stddev):
	return np.random.normal(loc=r, scale=stddev, size=1)[0]

def cp(tol_des, stddev):
	return tol_des / (3 * stddev)

def p_factor(cp_acq, cp_des):
	return cp_acq / cp_des
