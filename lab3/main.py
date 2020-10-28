from matplotlib import pyplot as plt
import networkx as nx
import gr
import cl_gen
import random

mutation = 70  # need to complete (in percents)*
num = 10
iteration = 5000
sons = 15
#chance_of_conn = 0.05#for 300
#chance_of_conn = 0.15#for 100
chance_of_conn = 0.3
G = gr.create_gr(num, chance_of_conn)
arr = cl_gen.Generation(num, G, mutation)
arr.first_gen_cr()


# print(arr.is_alive(arr.crossover(0, 1)))


def main(iter, array):
    def take_rand_parents(arrayN):
        rn1 = random.randint(0, len(arrayN.population) - 1)
        rn2 = random.randint(0, len(arrayN.population) - 1)
        # prevent dublicating
        while rn1 == rn2:
            rn2 = random.randint(0, len(arrayN.population) - 1)
        return rn1, rn2

    i = 0
    while i < iter:
        # find two random parents
        mother, father = take_rand_parents(array)
        array.crossover(mother, father, sons)
        i += 1
    #array.show_full_pop()
    array.find_kliks()
    print('pop: ', len(array.population))

main(iteration, arr)

for i in arr.kliks:
    print(i)
gr.avg_edges(G)
arr.population[0].first_gen_update(0,G)
for i in nx.find_cliques(G):
   print('asd', i)
