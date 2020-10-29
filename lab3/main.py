from matplotlib import pyplot as plt
import networkx as nx
import gr
import cl_gen
import random
import time

mutation = 100  # need to complete (in percents)*
num = 300
iteration = 3000
sons = 10
#chance_of_conn = 0.05   #for 300
chance_of_conn = 0.1#for 100
#chance_of_conn = 0.1#for 50
#chance_of_conn = 0.3
G = gr.create_gr(num, chance_of_conn)
arr = cl_gen.Generation(num, G, mutation)
arr.first_gen_cr()


# print(arr.is_alive(arr.crossover(0, 1)))


def main(iter, array, is_klika):

    is_klika = int(is_klika)

    def take_from_kliks(array):
        def look_for_in(mom):
            cnt1 = 0
            for j in array.population:
                if mom == array.population[cnt1].gen:
                    return cnt1
                cnt1 += 1
        cnt = 1
        array.find_kliks()
        for i in array.kliks:
            #print(i)
            if len(i) > 0:
                cnt += 1
        amount_kliks = cnt
        #print(cnt)
        if cnt == 2 or len(array.kliks[3]) <= 1:
            return take_rand_parents(array)
        rn_1 = random.randint(0, len(array.kliks[3]) - 1)
        pr1 = array.kliks[3][rn_1]
        mother =[]

        for i in range(0,array.quantity):
            if i in pr1:
                mother.append(1)
            else:
                mother.append(0)
        rn1 = look_for_in( mother)
        rn2 = random.randint(0, len(array.population) - 1)
        while rn1 == rn2:
            rn2 = random.randint(0, len(array.population) - 1)
        return rn1, rn2

    def take_rand_parents(arrayN):
        rn1 = random.randint(0, len(arrayN.population) - 1)
        rn2 = random.randint(0, len(arrayN.population) - 1)
        # prevent dublicating
        while rn1 == rn2:
            rn2 = random.randint(0, len(arrayN.population) - 1)
        return rn1, rn2
    decision = False
    i = 0
    while i < iter:
        #find two random parents
        # if random.randint(0, 1) == 1:
        #     mother, father = take_rand_parents(array)
        # else:
        #     mother, father = take_from_kliks(array)
        mother, father = take_from_kliks(array)
        #mother, father = take_rand_parents(array)

        array.crossover(mother, father, sons)
        i += 1
        array.find_kliks()
        if len(array.kliks[is_klika]) >= 1 :
            print("Yes",array.kliks[is_klika][0],'iter -', i)
            decision = True
            break

    if not decision:
        print('No such kliks')
    #array.show_full_pop()
    array.find_kliks()
    print('pop: ', len(array.population))

is_klika = input()
start_time = time.time()
main(iteration, arr, is_klika)

print("--- %s seconds ---" % (time.time() - start_time))
#for i in arr.kliks:
#    print(i)
gr.avg_edges(G)
arr.population[0].first_gen_update(0,G)
#arr.show_full_pop()
#for i in nx.find_cliques(G):
#   print('asd', i)
