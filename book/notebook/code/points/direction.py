def direction(p1, p2, p3):
	return  cross_product(p3.subtract(p1), p2.subtract(p1))
# checks if p3 makes left turn at p2
def left(p1, p2, p3):
	return direction(p1, p2, p3) < 0
# checks if p3 makes right turn at p2
def right(p1, p2, p3):
	return direction(p1, p2, p3) > 0
# checks if p1, p2 and p3 are collinear
def collinear(p1, p2, p3):
	return direction(p1, p2, p3) == 0