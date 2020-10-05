import packCl
import random

def createThings(num):
    arr = []
    for i in range(0, num):
        arr.append(packCl.Thing())
    return arr


def main(iteration):
    num_t = 100
    num_p = 100
    capacity = 250
    generation = []
    k_1 = 0.3
    k_2 = 0.4
    percent_mut = 10

    pack = packCl.Backpack(capacity)
    arr_things = createThings(num_t)
    generation = packCl.Generation(num_p, arr_things)
    generation.firstFill()

    generation.arr[1].count_param()
    #print(generation.arr[1].price)
    #print(generation.findBest())
    best_gen, record, max_size = generation.findBest()
    k = 0
    while k < iteration:

        ran_mother = random.randint(0, num_p - 1)
        father = best_gen
        s = generation.crossover(father, ran_mother, k_1, k_2)
        s = generation.mutation(s, percent_mut)
        newby = packCl.Decision(num_t, arr_things)
        newby.casual_ins(s)
        newby.count_param()
        #print(newby.price , newby.size)
        newby_price = newby.price
        newby_size = newby.size
        #print(generation.arr[len(generation.arr) - 1])
        if newby_size < capacity:
            generation.change_min_on(newby, newby_price)
        k += 1
        best_gen, record, max_size = generation.findBest()
        if k % 20 == 0:
            print(record)
        if record > 200:
            break

    print(record, max_size,generation.arr[best_gen].gen)
main(1000)
