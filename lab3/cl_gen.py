import random
import networkx as nx
import copy
from matplotlib import pyplot as plt


class Decision:
    def __init__(self, quantity):
        self.nodes = 1
        self.quantity = quantity
        self.gen = []
        self.klika_num = 0

#usual first_gen
    def first_gen(self, num):
        for i in range(0, self.quantity):
            if i != num:
                self.gen.append(0)
            else:
                self.gen.append(1)
        #print(self.gen)
#updated


    def first_gen_update(self, num, G):
        ran_num = random.randint(0, len(nx.to_dict_of_dicts(G)[num]) - 1)
        pair_arr = nx.to_dict_of_dicts(G)[num]
        cnt = 0
        pair = 0
        for i in pair_arr:
            if cnt == ran_num:
                pair = i
            cnt += 1
        for i in range(0, self.quantity):
            if i != num and i != pair :
                self.gen.append(0)
            else:
                self.gen.append(1)

    def new_gen(self, new_gen):
        self.gen = new_gen

    def find_klika(self):
        self.klika_num = 0
        for i in self.show_as_norm():
            self.klika_num += 1

    def show_as_norm(self):
        loc = []
        count = 0
        for i in self.gen:
            if i == 1:
                loc.append(count)
            count += 1
        return loc


class Generation:
    def __init__(self, quantity, G, chance_mutation):
        self.quantity = quantity
        self.population = []
        self.graph = G
        self.kliks = [[],[],[],[],[],[],[],[],[],[],[]]
        self.m_chance = chance_mutation

    def first_gen_cr(self):
        for i in range(0, self.quantity):
            self.population.append('')
            self.population[i] = Decision(self.quantity)
            self.population[i].first_gen_update(i, self.graph)

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
                #choose whose genom it will take
                a = random.randint(1, 2)
                if a == 1:
                    new_arr.append(self.population[first_id].gen[i])
                elif a == 2:
                    new_arr.append(self.population[sec_id].gen[i])
                i += 1
            #print(new_arr)
            #new_arr = self.mutation_update(new_arr, self.m_chance)
            new_arr = self.mutation(new_arr, self.m_chance)
            #print(new_arr)
            #check if it already exist in decisions
            k = 0
            already_exist = False

            while k < len(self.population):
                if new_arr == self.population[k].gen:
                    already_exist = True
                k += 1
            if self.is_alive(new_arr) and not already_exist:
                #print('1', self.population[sec_id].gen)
                #print('2', self.population[first_id].gen)
                #print(new_arr)
                self.population.append(Decision(self.quantity))
                self.population[len(self.population) - 1].new_gen(new_arr)
                self.population[len(self.population) - 1].find_klika()

                # if self.population[len(self.population) - 1].klika_num >= 4:
                #self.show_full_pop()
                #print(self.population[len(self.population) - 1].show_as_norm())



    def find_kliks(self):
        loc = self.quantity
        max_klika = 0

        for i in self.population:
            i.find_klika()
            if max_klika < i.klika_num:
                max_klika = i.klika_num
            self.kliks[i.klika_num].append(i.show_as_norm())


# usual mutation

    def mutation(self, arr, percent):
        ran = random.randint(1, 100)
        old = copy.copy(arr)
        new = copy.copy(arr)
        if ran < percent:
            ran_mut = random.randint(0, self.quantity - 1)
            if new[ran_mut] == 1:
                new[ran_mut] = 0
            else:
                new[ran_mut] = 1
        if self.is_alive(new):
            return new
        else:
            return old

#updated mutation
    def mutation_update(self, arr, percent  ):
        arr_for_rand = []
        arr_for_res = []
        cnt = 0
        old = copy.copy(arr)
        for j in arr:
            if j == 1:
                arr_for_rand.append(cnt)
            cnt += 1
        if len(arr_for_rand) > 1:
            ran_num = random.randint(0, len(arr_for_rand) - 1)
            pair_arr = nx.to_dict_of_dicts(self.graph)[arr_for_rand[ran_num]]
            #print(arr_for_rand[ran_num])
            #print(pair_arr)
            cnt1 = 0
            for j in arr:
                if j == 1:
                    arr_for_res.append(cnt)
                cnt1 += 1
            #соединенные с случайно выбраным из списка законекченных
            ran_num2 = random.randint(0, len(arr_for_res) - 1)
            #print(ran_num2)
            new = []
            cnt3 = 0
            for i in  arr:
                if i == 1 or cnt3 == ran_num2:
                    new.append(1)
                else:
                    new.append(0)
                cnt3 += 1
            if self.is_alive(new):
                return new
            else:
                return old
        else:
            return old


    def show_full_pop(self):
        for i in self.population:
            print('pop', i.show_as_norm(), i.klika_num)
