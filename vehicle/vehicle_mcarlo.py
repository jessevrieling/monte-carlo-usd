import csv
import math
import numpy as np
import stat_util

# forward accuracy is 0.02m (2cm)
acc_pos = 0.02

# angle accuracy is 2 degrees
acc_dir = 2

stddev_pos = acc_pos / 3
stddev_dir = acc_dir / 3

# order matters so tuple of tuples
pattern = (
    (2, -90),  # move North 2, turn East
    (2, 90),   # move East 2, turn North
    (2, 90),   # move North 2, turn West
    (1, -90),  # move West 1, turn North
    (3, 90),   # move North 3, turn West
    (1, 0)     # move West 1, end facing West
)

def write_csv(arr):
		data = []

		for i in range(len(arr)):
			data.append({'n': i + 1, 'd_nom': arr[i]})

		with open('simulation.csv', 'w', newline='') as csvfile:
			fieldnames = ['n', 'd_nom']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			writer.writerows(data)

def move_to_end():
	# we start at (0, 0) and facing 90 ± 2 degrees (north)
	pos = (0, 0)
	direction = stat_util.randnorm(90, stddev_dir)

	# apply every motion in the pattern to the position
	for motion in pattern:
		scalar = stat_util.randnorm(motion[0], stddev_pos);

		x_cur = pos[0]
		y_cur = pos[1]

		x_new = pos[0] + scalar * np.cos(np.deg2rad(direction))
		y_new = pos[1] + scalar * np.sin(np.deg2rad(direction))

		pos = (x_new, y_new)
		direction += stat_util.randnorm(motion[1], stddev_dir)

	return pos

def simulate(n):
	distances = []

	for i in range(n):
		distances.append(math.dist(move_to_end(), (0, 7)))

	write_csv(distances)

simulate(1000)
