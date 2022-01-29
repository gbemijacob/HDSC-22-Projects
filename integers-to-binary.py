# binn = str(bin(13))
# print(binn)

# pet = str(format(13, "b"))
# print(pet)

# pet1 = str("{0:08b}".format(13, "b"))
# print(pet1)

def count_bits(n):
    total_count = 0
    binary = str(format(n, "b"))
    for digit in binary:
        if digit == "1":
            total_count += 1
    return total_count

print(count_bits(111))