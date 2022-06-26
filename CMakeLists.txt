cmake_minimum_required(VERSION 3.0)
project(cs50x C)

set(CMAKE_C_STANDARD 11)

SET(CMAKE_C_FLAGS     "-lcs50 -lm")

add_executable(hello src/pset1/hello/hello.c)
add_executable(cash src/pset1/cash/cash.c)
add_executable(mario src/pset1/mario/mario.c)

add_executable(caesar src/pset2/caesar/caesar.c)
add_executable(readability src/pset2/readability/readability.c)
add_executable(scrabble src/pset2/scrabble/scrabble.c)
