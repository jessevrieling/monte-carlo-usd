import csv
import v_util
import stat_util
import statistics

vin = 100
vout_nom = 20
r1_nom = 200
r2_nom = 50
rtol = 5
tol_des = 0.5 #+- 0.5v of nominal
cp_desired = 2

print(f"resistance R1: {r1_nom} Ohm")
print(f"resistance R2: {r2_nom} Ohm\n")

def simulate(vin, vout_nom, r1_nom, r2_nom, tol_des, cp_desired, rtol, n_sample, n_run):
	cp_achieved = 0
	stddevr1 = stat_util.stddevr(r1_nom, rtol)
	stddevr2 = stat_util.stddevr(r2_nom, rtol)

	for i in range(n_run):
		vout = v_util.voltdivout(vin, r1_nom, r2_nom, stddevr1, stddevr2, n_sample)
		stddev_vout = statistics.stdev(vout)
		cp_achieved = stat_util.cp(tol_des, stddev_vout)
		p_factor = stat_util.p_factor(cp_achieved, cp_desired)
		
		#process is centralized so we can use the same p factor on r1 and r2
		stddevr1 *= p_factor
		stddevr2 *= p_factor
		rtol = stat_util.percstddev(r1_nom, stddevr1)

	print(f"cp achieved: {cp_achieved}")

	return rtol

tol_perc = simulate(vin, vout_nom, r1_nom, r2_nom, tol_des, cp_desired, rtol, 1000, 1000);

print(f"tolerance percentage: {tol_perc}")
