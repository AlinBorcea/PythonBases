# x -> decimal number
# b -> base to represent x in
def x_in_base_b(x, b):
    nums = []
    while x // b != 0:
        nums.append(x % b)
        x //= b

    nums.append(x)
    return nums


# nums -> representation of decimal in base b
# b -> base
def decimal(nums, b):
    sum = 0
    p = 1
    for x in nums:
        sum += p * x 
        p *= b

    return sum


dec = int(input("decimal = "))
base = int(input("base = "))

decimal_in_b = x_in_base_b(dec, base)
num_from_b = decimal(decimal_in_b, base)

print("nums is: " + str(decimal_in_b) + "\nnum is: " + str(num_from_b))
