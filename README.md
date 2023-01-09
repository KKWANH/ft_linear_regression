# ft_linear_regression

## How to run
1. **First, clone the repository.**
```Shell
git clone https://github.com/KKWANH/linear_regression
```

2. **Move to the repository that you just cloned.**
```Shell
cd linear_regression
```

3. You can run everything in our repository by the command; `make`
```Shell
# To get informations about specitfic make keywords
make help
```
```Shell
# Remove temporary files
make clean
```
```Shell
# Setup python virtual environmetns
make setup
```
```Shell
# Enable the virtual env that you just made
make env
```
```Shell
# Predicting.
#   If you input the mileage(km), and you will receive predicted price.
make predict
```
```Shell
# Training
#   Train and make [parameter.dat] as a result.
make train
```