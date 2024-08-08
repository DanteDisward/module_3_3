def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(43)
print_params('ok', 789, 'turle')
print_params(c=52, b=False, a=22)

values_list = [2.45, "Hello", True]
values_dict = {'a': 65, 'b': False, 'c': 45.6}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['Bye', 45]
print_params(*values_list_2, 42)