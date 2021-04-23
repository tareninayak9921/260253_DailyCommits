def multiply_list(items):
    product = 1
    for x in items:
        product *= x
    return product
print(multiply_list([1,2,-8]))