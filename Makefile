# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kimkwanho <kimkwanho@student.42.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/28 12:28:15 by kimkwanho         #+#    #+#              #
#    Updated: 2022/12/29 17:24:54 by kimkwanho        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME 		=	ft_linear_regression

SRCS 		=	srcs/
SETUP_SRC	=	srcs/setup_env.sh

all:
	clean
	setup
	run

clean:
	rm -rf srcs/__pycache__
	rm -rf srcs/ft_env
	rm -rf srcs/parameter.dat

setup:
	sh $(SETUP_SRC)

run:
	python $(SRCS)