class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def subtract(self, p):
    	return Point(self.x - p.x, self.y - p.y)
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'