import random
import copy


class Backpack:
    def __init__(self, size):
        self.size = size
        self.arr = []


class Decision:
    def __init__(self, quantity, things):
        self.gen = []
        self.quantity = quantity
        self.size = 0
        self.price = 0
        self.things = things

    def firstGen(self, num):
        for i in range(0, self.quantity):
            if i != num:
                self.gen.append(0)
            else:
                self.gen.append(1)

    def count_param(self):
        sum_s = 0
        sum_p = 0
        for i in range(0, len(self.gen)):
            if self.gen[i] == 1:
                sum_s += self.things[i].size
                sum_p += self.things[i].price
        self.size = sum_s
        self.price = sum_p

    def casual_ins(self, arr):
        self.gen = arr


class Generation:
    def __init__(self, quantity, things):
        self.quantity = quantity
        self.arr = []
        self.things = things

    def firstFill(self):
        for i in range(0, self.quantity):
            self.arr.append(Decision(self.quantity, self.things))
            self.arr[i].firstGen(i)

    def findBest(self):
        # id of max decision
        max_decis = 0
        max_price = 0
        for i in range(0, self.quantity):
            self.arr[i].count_param()
            if self.arr[i].price > max_price:
                max_decis = i
                max_price = self.arr[i].price
                max_size = self.arr[i].size
        return max_decis, max_price, max_size

    def mutation(self, arr, percent):
        ran = random.randint(1, 100)
        old = copy.copy(arr)
        if ran < percent:
            arr_0 = []
            arr_1 = []
            for i in range(0, self.quantity - 1):
                if arr[i] == 0:
                    arr_0.append(i)
                else:
                    arr_1.append(i)
            if len(arr_1) >= 1:
                ran_0 = random.randint(0, len(arr_0) - 1)
                ran_1 = random.randint(0, len(arr_1) - 1)
            else:
                ran_0 = random.randint(0, len(arr_0) - 1)
                ran_1 = 0
            if len(arr_1) != 0:
                #print(arr_1, ran_1)
                #print(arr_1[ran_1])
                arr[arr_0[ran_0]] = 1
                arr[arr_1[ran_1]] = 0
                #print('arr of pos', arr_1, arr_0)
                #print('mutation ', arr_1[ran_1], arr_0[ran_0])
                #print(old, arr)

        return arr

    def crossover(self, first_id, sec_id, koef_1, koef_2):
        i = 0
        new_arr = []
        # print(self.arr[first_id].gen)
        # print(self.arr[sec_id].gen)
        while i < len(self.arr[first_id].gen):
            # print(first_id, sec_id)
            # print(i, self.arr[sec_id].gen)
            if i < koef_1 * len(self.arr[first_id].gen):
                new_arr.append(self.arr[first_id].gen[i])
            elif i < (koef_1 + koef_2) * len(self.arr[sec_id].gen):
                new_arr.append(self.arr[sec_id].gen[i])
            else:
                new_arr.append(self.arr[first_id].gen[i])
            i += 1
        return new_arr

    def change_min_on(self, arr2, new_price):
        min_decis = 99
        min_price = 99
        for i in range(0, self.quantity):
            self.arr[i].count_param()
            if self.arr[i].price < min_price:
                min_decis = i
                min_price = self.arr[i].price
        if new_price > min_price:
            self.arr[min_decis] = arr2

        return min_decis, min_price


class Thing:
    def __init__(self):
        self.size = random.randint(1, 25)
        self.price = random.randint(2, 30)
