#Building an exponent function that will basically allow us to take a certain number and raise it to a specific power
#Basic function for power in python is usually:
print(2**3)
#Now we will do it using for loop

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3, 2))
