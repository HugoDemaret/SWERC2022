def left_turn(a,b,c):
	return (a[0]-c[0]) * (b[1]-c[1]) - (a[1]-c[1]) * (b[0]-c[0]) > 0
	# If floats are used, instead of 0 test if in [0-10E-7,0+10E-7]