import csv
import res_util as ru

def voltdivout(vin, r1_nom, r2_nom, stddevr1, stddevr2, n):
	vout = []

	for i in range(n):
		r1 = ru.randrnorm(r1_nom, stddevr1)
		r2 = ru.randrnorm(r2_nom, stddevr2)

		vout.append(ru.vdivout(vin, r1, r2))

	return vout

def write_csv(arr):
	data = []

	for i in range(len(arr)):
		data.append({'n': i + 1, 'vout': arr[i]})

	with open('simulation.csv', 'w', newline='') as csvfile:
		fieldnames = ['n', 'vout']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		writer.writerows(data)

vin = 100
r1_nom = 200
r2_nom = 50

stddevr1 = 5 / 100 * r1_nom / 3
stddevr2 = 5 / 100 * r2_nom / 3

print(f"resistance R1: {r1_nom} Ohm")
print(f"resistance R2: {r2_nom} Ohm\n")
print(f"stddev R1: {stddevr1}")
print(f"stddev R2: {stddevr2}\n")

vout = voltdivout(100, r1_nom, r2_nom, stddevr1, stddevr2, 10)
print("creating csv...")
write_csv(vout)
print("done");
