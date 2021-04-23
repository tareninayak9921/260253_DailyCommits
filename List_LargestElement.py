def maximum_no( list ):
    max = list[ 0 ]
    for i in list:
        if i > max:
            max = i
    return max
print(maximum_no([21, 12 , 5 ,7]))