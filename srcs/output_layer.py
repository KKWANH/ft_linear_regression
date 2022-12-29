# --------------------------------------------------------------------
# importing
import numpy

# w(weight) = θ_1, b(bias) = θ_0
class OutputLayer:
	def __init__(self, _w_b_width, len_in, len_out):
		self.w_b_width = _w_b_width
		self.w = self.w_b_width * numpy.random.randn(len_in, len_out) # 가중치(행렬)
		self.b = self.w_b_width * numpy.random.randn(len_out)

	def forward(self, _x):
		self.x = _x
		tmp = numpy.dot(_x, self.w) + self.b
		self.y = tmp
	
	def backward(self, _t):
		delta = self.y
		self.w_grad = numpy.dot(self.x.T, delta)
		self.b_grad = numpy.sum(delta, axis=0)
		self.x_grad = numpy.dot(delta, self.w.T)

	def update(self, _l_rate, _length):
		self.w -= _l_rate * (1/_length) * self.w_grad
		self.b -= _l_rate * (1/_length) * self.b_grad