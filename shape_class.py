class  shape (object):
	

	def __init__(self):
		pass

	def area(self):
		pass

	def perimeter(self):
		pass


class circle(shape):
	
	def __init__(self, r,c):
		self.radius = r
		self.color = c

	def area(self):

		if self.radius < 0:
			return "Invalid radius"
		else:
			return 22/7 * self.radius * self.radius

	def perimeter(self):
		if self.radius < 0:

			return "Invalid radius"
		else:

			return 22/7 * 2 * self.radius

class rectangle(shape):

	def __init__(self,c,h,w):

		self.color = c
		self.width = w
		self.height = h

	def area(self):

		if self.width, self.height < 1 :

			return "Invalid radius"
		else:

			return self.width * self.height

	def perimeter(self):
		if self.width, self.height < 1:

			return "Invalid radius"
		else:
		
			return (self.width + self.height)*2

class triangle(shape):

	def __init__(self,h,b,d,c):

		self.height = h
		self.base = b
		self.d2 = d
		self.color = c

	def area(self):

		if self.base, self.height, self.d2 < 1 :

			return "Invalid radius"
		else:

			return 1/2*self.base * self.height

	def perimeter(self):

		if self.base, self.height, self.d2 < 1 :

			return "Invalid radius"
		else:

			return self.height+ self.base+self.d2.

		
		