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

add_executable(plurality src/pset3/plurality/plurality.c)
add_executable(runoff src/pset3/runoff/runoff.c)

add_executable(volume src/pset4/volume/volume.c)
add_executable(filter src/pset4/filter/filter.c src/pset4/filter/helpers.c)
add_executable(recover src/pset4/recover/recover.c)
