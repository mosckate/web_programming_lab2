import random

def memorize_func(f):
    memo = dict()
    def func(*args):
        if args not in memo:
            memo[args] = f(*args)
        return memo[args]
    return func

@memorize_func
def func1(var):
    #print("First")
    l = list(str(var))
    k = 0
    for i in range(len(l)//2):
        if l[i] == l[-i-1]:
            k = k + 1
    if k == len(l)//2:
        return True
    else:
        return False

def func2(list_all):
    list1 = []
    list2 = []
    list3 = []
    for i in range(len(list_all)):
        if list_all[i] % 2 == 0:
            list1.append(list_all[i])
        if list_all[i] % 3 == 0:
            list2.append(list_all[i])
        if list_all[i] % 5 == 0:
            list3.append(list_all[i])
    return list1, list2, list3

def func3(var):
    list_var = list(str(abs(var)))
    var_output = []
    for i in range(len(list_var)-1, -1, -1):
        var_output.append(list_var[i])
    if var > 0:
        return int("".join(map(str, var_output)))
    else:
        return -int("".join(map(str, var_output)))

def func4(num, power):
    approx = random.randint(1, 101) % 10
    eps = 0.001
    del_x = 2147483647
    better = 0.0
    while (del_x > eps):
        better = ((power - 1.0) * approx + num / pow(approx, power - 1)) / power
        del_x = abs(better - approx)
        approx = better
    return better

def func5(var):
    if var < 2:
        return False
    k = 0
    for i in range(1, var + 1):
        if var % i == 0:
            k = k + 1
    if k == 2:
        return True
    else:
        return False
       
print(func1(121))
print(func1(1234))
print(func2([3, 67, 54, 100, 15]))
print(func3(-90))
print(func4(27, 3))
print(func5(3))
print(func5(100))