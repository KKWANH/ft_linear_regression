# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kkim <kkim@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/28 12:28:15 by kimkwanho         #+#    #+#              #
#    Updated: 2023/01/03 16:06:59 by kkim             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

all:
	@make help

clean:
	@printf "\033[1m\033[31m[Clean]\033[0m\t Remove previous files\n"
	@rm -rf __pycache__
	@rm -rf ft_env
	@rm -rf parameter.dat

setup:
	@printf "\033[1m\033[32m[Setup]\033[0m\t Setting virtual-environment\n"
	@sh "srcs/setup.sh"

env:
	@printf "\033[1m\033[32m[Env]\033[0m\t Running virtual-environment.\n"
	@source "ft_env/bin/activate"
	@printf "\033[1m\033[32m[Env]\033[0m\t If the next path is not in \033[1m\033[96mft_env\033[0m, this means there are some \033[1m\033[91merror\033[0m on this progress.\n"
	@printf "\033[1m\033[32m[Env]\033[0m\t \033[1m\033[4m"
	@which python
	@printf "\033[0m"

predict:
	@printf "\033[1m\033[34m[Read]\033[0m\t Running the predict.py code\n"
	python3 "srcs/predict.py"

train:
	@printf "\033[1m\033[34m[Train]\033[0m\t Running the training.py code\n"
	python3 "srcs/training.py"

help:
	@printf "\033[1m\033[33m[Help]\033[0m\t \033[4m\033[1mthere are 5 options.\033[0m\n"
	@printf "\033[1m\033[33m[Help]\033[0m\t \033[31m[make clean]\033[0m remove pycache, env folder, and parameter.dat\n"
	@printf "\033[1m\033[33m[Help]\033[0m\t \033[32m[make setup]\033[0m setup the virtual python environment\n"
	@printf "\033[1m\033[33m[Help]\033[0m\t \033[32m[make env]\033[0m   let the python run in the folder ft_env\n"
	@printf "\033[1m\033[33m[Help]\033[0m\t \033[34m[make read]\033[0m  Run reading.py\n"
	@printf "\033[1m\033[33m[Help]\033[0m\t \033[34m[make train]\033[0m Run training.py\n"
	@printf "\033[1m\033[33m[Help]\033[0m\t \n"
	@printf "\033[1m\033[33m[Help]\033[0m\t We recommend you to execute this project by this order.\n"
	@printf "\033[1m\033[33m[Help]\033[0m\t \033[1m\033[4m\033[31mmake clean\033[0m ??? \033[1m\033[4m\033[32mmake setup\033[0m ??? \033[1m\033[4m\033[32mmake env\033[0m ??? \033[1m\033[4m\033[34mmake read\033[0m ??? \033[1m\033[4m\033[34mmake train\033[0m ??? \033[1m\033[4m\033[34mmake read\033[0m\n"