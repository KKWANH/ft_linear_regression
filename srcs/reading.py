# --------------------------------------------------------------------
# importing
from pathlib import Path
from util import colors as c

# --------------------------------------------------------------------
# utilization functions

# is_float(num)
# 	return True if the input number is float
#	if the num cause ValueError, returns False
def is_float(_num):
	try:
		float(_num)
		return True
	except ValueError:
		return False

# pre-process(x, x_min, x_max)
#	set the window of x as 0 to 1
#	 0~1 normalize	 : similar with sigmoid
#	-1~1 standardize : similar with tanh
def normalize(_x, _x_min, _x_max):
	if (_x_min == 0 and _x_max == 0):
		return _x
	return (_x - _x_min) / (_x_max - _x_min)

# get_params(void)
def get_params():
	# variable setting
	file_name = 'parameter.dat'
	path = Path(file_name)
	arrayList = []

	# Error check
	# 	return 0,0,0,0 if the file is not valid
	if (not path.is_file()):
		return 0,0,0,0

	# reading file
	with open(file_name, 'r') as file:
		for line in file.readlines():
			if (is_float(line.split()[0]) == False):
				continue
			arrayList.extend(line.split())
	file.close()

	weight = arrayList[0]
	bias = arrayList[1]
	x_min = arrayList[2]
	x_max = arrayList[3]

	# error check
	if (len(arrayList) != 4): 
		return 0,0,0,0
	if (not is_float(weight) or
		not is_float(bias) or
		not is_float(x_min) or
		not is_float(x_max)):
		return 0,0,0,0
	
	return float(weight), float(bias), float(x_min), float(x_max)

# --------------------------------------------------------------------
# main start

# variable setting
theta1, theta0, x_min, x_max  = get_params()
print(f"{c.CYAN}[i]      [params]{c.RESET}        {theta0}, {theta1}, {x_min}, {x_min}")

# mileage input
while True:
	try:
		# 👇️ use int() instead of float
		# if you only accept integers
		x = float(input(f"{c.PURPLE}[?]      [mileage]{c.RESET}       "))
		if (x > 0):
			print(f"{c.CYAN}[i]      [mileage]{c.RESET}       {x}")
			break
		else:
			print(f"{c.YELLOW}[X]      [WARNING]{c.RESET}       Please enter a positive number.")
	except ValueError:
		print(f"{c.YELLOW}[X]      [WARNING]{c.RESET}       Please enter a number.")

# mileage normalize 
normalizedX = normalize(x, x_min, x_max)
print(f"{c.CYAN}[i]      [normalized x]{c.RESET}  {x} →", "{0:.5f}".format(normalizedX))
y = theta0 + theta1 * normalizedX

# result 
if y >= 0:
	print(f"{c.GREEN}[i]      [estimate]{c.RESET}     ", "{0:.3f}".format(y))
else:
	print(f"{c.YELLOW}[X]      [estimate]{c.RESET}     ", "{0:.3f}".format(y), f"{c.RED}[this number is meaningless, out of range]{c.RESET}")