from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

x = [] # distance along x-axis (nm)
y = [] # distance along y-axis (nm)
z = [] # band energy (eV)

with open('bandedge3d.fld') as f:
	lines = iter(f)

	newLineNum = 0

	for line in lines:
		
		# if line is newline or space-newline
		if str(line)[:1] == '\n' or str(line)[:2] == ' \n':
			newLineNum += 1

		# parse x and y values
		# if 5th char is '.'
		if str(line)[4:5] == '.':
			if newLineNum == 3:
				x.append(str(line)[3:-1])
			if newLineNum == 4:
				y.append(str(line)[3:-1])

		# parse z values
		# if 6th char is '.'
		# skip 5th newline, which begins z positions
		if str(line)[5:6] == '.' and newLineNum == 6:
			z.append(str(line)[4:17])