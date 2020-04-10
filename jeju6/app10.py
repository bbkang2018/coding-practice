def create_to_power_fuction(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = result * base_num
    return result

print(create_to_power_fuction(3,5))


