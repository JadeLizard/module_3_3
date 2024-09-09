def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
print_params() # можно вызвать все аргументы по умолчанию
# print_params(a,b) - ошибка, нельзя вызвать 2 из 3 аргументов по умолчанию
print_params(a=2) # можно вызвать 1 именованный аргумент, и даже заменить его на иной

values_list = ['Yep', False, 3.14]
values_dict = {'a': 'chill', 'b':666, 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ('cheese', 80085)
print_params(*values_list_2, 42) #могу сначала вызвать список, и включить в него новый позиционный аргумент