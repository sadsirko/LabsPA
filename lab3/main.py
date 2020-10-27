from matplotlib import pyplot as plt
import networkx as nx
import gr
import cl_gen
import random

mutation = 0.4#need to complete
kliks = []    #
num = 10
iteration = 300
sons = 4
G = gr.print_hi(num)

arr = cl_gen.Generation(num, G)
arr.first_gen_cr()


# print(arr.is_alive(arr.crossover(0, 1)))


def main(iter, array):
    def take_rand_parents(array):
        rn1 = random.randint(0, len(array.population) - 1)
        rn2 = random.randint(0, len(array.population) - 1)
        # prevent dublicating
        while rn1 == rn2:
            rn2 = random.randint(0, len(array.population) - 1)
        return rn1, rn2

    i = 0
    while i < iter:
        # find two random parents
        mother, father = take_rand_parents(arr)
        arr.crossover(mother, father, sons)
        i += 1


main(iteration, arr)
loc = num
for i in arr.population:
    if loc < 0:
        print(i.gen)
    loc -= 1