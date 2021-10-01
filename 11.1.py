def pro(x):
    if x % 5 == 0:
        return True
    else:
        return False


data_list = [5, 12, 25, 523, 525, 345, 4, 245, 87, 12]

print(str(filter(pro, data_list)))

new_data_list = [i for i in filter(pro, data_list)]
print(new_data_list)
