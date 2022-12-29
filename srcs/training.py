# --------------------------------------------------------------------
# importing
import pandas
import numpy
import matplotlib.pylab as plt

from output_layer import OutputLayer


# --------------------------------------------------------------------
# utilization functions

# get_cost(_y, _y_pred)
# 	RMSE, (Root Mean Square Error)
# 		[Error] means the diffrence between real y and the prediction of y
#		RMSE calculate the cost as [sqrt(mean(square(y - y_prediction)))]
# 		
def get_cost(_y, _y_pred):
	N = len(_y)
	cost = numpy.sqrt(numpy.sum(numpy.square(_y - _y_pred)) / N)
	return cost

# normalize(x)
# 	set x's range as 0~1
def normalize(_x):
	x_max = numpy.max(_x)
	x_min = numpy.min(_x)
	# print(f"[D] [normalize]\t  {_x, x_min, x_max},  {_x - x_min},  {x_max - x_min},  {(_x - x_min) / (x_max - x_min)}")
	return (_x - x_min) / (x_max - x_min)

#회귀식 입력-> 입력층 (-> 은닉층) -> 출력층 -> 출력
#은닉층의 활성화 함수: 시그모이드 함수
#출력층의 활성화 함수: 항등 함수
#손실 함수: 오차제곱합
#최적화 알고리즘: 확률적 경사 하강법

# preparation
readed_data	= pandas.read_csv("./data.csv")
input		= readed_data['km'].to_numpy()
x_max		= numpy.max(input)
x_min		= numpy.min(input)
answer		= readed_data['price'].to_numpy()
input		= normalize(input)
length		= len(answer)

# gradient_descent(_input, _answer, _length)
def gradient_descent(_input, _answer, _length):
	# setting
	len_in	= 1			# count of input neuron layer
	len_out	= 1			# count of output neuron layer
	w_b_width = 0.01
	l_rate = 0.05		# learning rate
	epoch = 2001		# epoch
	interval = 40		# printing interval

	# initialization
	output_layer = OutputLayer(w_b_width, len_in, len_out)
	plot_x = []
	plot_y = []
	plot_w = []
	plot_b = []

	# training
	for i in range(epoch):
		# index shuffle
		i_random = numpy.arange(_length)
		numpy.random.shuffle(i_random)

		for j in i_random:
			x = _input[j:j+1]	# input
			t = _answer[j:j+1]	# answer

			# print(f"[D] [reshape]\t  {x} vs {x.reshape(1, 1)}")
			output_layer.forward(x.reshape(1, 1))
			output_layer.backward(t.reshape(1, 1))
			output_layer.update(l_rate, _length)
	
		if i != 0 and i % interval == 0:
			_w = output_layer.w.reshape(-1)[0]
			_b = output_layer.b.reshape(-1)[0]
			_pred = _w * _input + _b
			_rmse = get_cost(answer, _pred)

			plot_x.append(i)
			plot_y.append(_rmse)
			plot_w.append(_w)
			plot_b.append(_b)

			print(	f"[Epoch]",		 "[{0:4}/{1:4}]  ".format(i, epoch),
					f"[RMSE]",		 "[{:.5f}]  ".format(_rmse),
					f"[weight/θ_1]", "[{:.5f}]  ".format(_w),
					f"[bias/θ_0]",	 "[{:.5f}]  ".format(_b))

	plt.plot(plot_x, plot_y, marker="+", color="red",	label="RMSE")
	plt.plot(plot_x, plot_y, marker="*", color="green", label="weight/θ_1")
	plt.plot(plot_x, plot_y, marker=".", color="gray",	label="bias/θ_0")
	plt.xlabel("epoch")
	plt.ylabel("RMSError")
	plt.legend()
	plt.show()

	return output_layer.w.reshape(-1)[0], output_layer.b.reshape(-1)[0]

w, b = gradient_descent(input, answer, length)

print(f"θ0 = {b}, θ1 = {w}")
pred = w * input + b
print(f"RMSError {str(get_cost(answer, pred))}")

plt.plot(input, pred, marker="+", color="blue", label="y_pred")
plt.scatter(input, answer, marker="+", label="y_real")
plt.xlabel(f"normalized mileage({x_min}km ~ {x_max}km) to (0 ~ 1)")
plt.ylabel("price")
plt.legend()
plt.show()

with open("parameter.dat", "w") as file:
	file.write("{0:.5f} {1:.5f} {2:.1f} {3:.1f}\n".format(w, b, x_min, x_max))
file.close()



