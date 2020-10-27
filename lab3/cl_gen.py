import random
import networkx as nx
from matplotlib import pyplot as plt


class Decision:
    def __init__(self, quantity):
        self.nodes = 1
        self.quantity = quantity
        self.gen = []
        self.klika_num = 0

    def first_gen(self, num):
        for i in range(0, self.quantity):
            if i != num:
                self.gen.append(0)
            else:
                self.gen.append(1)

    def new_gen(self, new_gen):
        self.gen = new_gen

    def find_klika(self):
        for i in self.gen:
            if i == 1 :
                self.klika_num += 1


class Generation:
    def __init__(self, quantity, G):
        self.quantity = quantity
        self.population = []
        self.graph = G

    def first_gen_cr(self):
        for i in range(0, self.quantity):
            self.population.append('')
            self.population[i] = Decision(self.quantity)
            self.population[i].first_gen(i)

    def is_alive(self, inhabitant):

        i = 0
        j = 0
        loc = 0
        while i < len(inhabitant):
            if inhabitant[i] == 1:
                while j < len(inhabitant):
                    a = j in nx.to_dict_of_dicts(self.graph)[i]
                    b = inhabitant[j] == 1
                    # is not empty
                    if (not a) and j != i and b:
                        return False
                    # is not th only one
                    if a and j != i and b:
                        loc += 1
                    j += 1
            i += 1
            j = 0
        if loc == 0:
            return False
        return True

    def crossover(self, first_id, sec_id, sons):
        i = 0
        new_arr = []
        # print(self.population[first_id].gen)
        # print(self.population[sec_id].gen)
        for j in range(0, sons):
            while i < self.quantity:
                # print(first_id, sec_id)
                # print(i, self.population[sec_id].gen)
                a = random.randint(1, 2)

                if a == 1:
                    new_arr.append(self.population[first_id].gen[i])
                elif a == 2:
                    new_arr.append(self.population[sec_id].gen[i])
                i += 1

            #check if it already exist in decisions
            k = 0
            already_exist = False
            while k < len(self.population):
                if new_arr == self.population[k].gen:
                    already_exist = True
                k += 1
            if self.is_alive(new_arr) and not already_exist:
                self.population.append(Decision(self.quantity))
                self.population[len(self.population) - 1].new_gen(new_arr)

    # def findBest(self):
    #     # id of max decision
    #     max_decis = 0
    #     max_price = 0
    #     for i in range(0, self.quantity):
    #         self.arr[i].count_param()
    #         if self.arr[i].price > max_price:
    #             max_decis = i
    #             max_price = self.arr[i].price
    #             max_size = self.arr[i].size
    #     return max_decis, max_price, max_size

    # def mutation(self, arr, percent):
    #     ran = random.randint(1, 100)
    #     old = copy.copy(arr)
    #     if ran < percent:
    #         arr_0 = []
    #         arr_1 = []
    #         for i in range(0, self.quantity - 1):
    #             if arr[i] == 0:
    #                 arr_0.append(i)
    #             else:
    #                 arr_1.append(i)
    #         if len(arr_1) >= 1:
    #             ran_0 = random.randint(0, len(arr_0) - 1)
    #             ran_1 = random.randint(0, len(arr_1) - 1)
    #         else:
    #             ran_0 = random.randint(0, len(arr_0) - 1)
    #             ran_1 = 0
    #         if len(arr_1) != 0:
    #             #print(arr_1, ran_1)
    #             #print(arr_1[ran_1])
    #             arr[arr_0[ran_0]] = 1
    #             arr[arr_1[ran_1]] = 0
    #             #print('arr of pos', arr_1, arr_0)
    #             #print('mutation ', arr_1[ran_1], arr_0[ran_0])
    #             #print(old, arr)
    #
    #     return arr

    #
    # def change_min_on(self, arr2, new_price):
    #     min_decis = 99
    #     min_price = 99
    #     for i in range(0, self.quantity):
    #         self.arr[i].count_param()
    #         if self.arr[i].price < min_price:
    #             min_decis = i
    #             min_price = self.arr[i].price
    #     if new_price > min_price:
    #         self.arr[min_decis] = arr2
    #
    #     return min_decis, min_price
