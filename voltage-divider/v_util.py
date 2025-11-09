import stat_util

def vdivout(vin, r1, r2):
	return r2 / (r1 + r2) * vin

def voltdivout(vin, r1_nom, r2_nom, stddevr1, stddevr2, n):
	vout = []

	for i in range(n):
		r1 = stat_util.randrnorm(r1_nom, stddevr1)
		r2 = stat_util.randrnorm(r2_nom, stddevr2)

		vout.append(vdivout(vin, r1, r2))

	return vout
