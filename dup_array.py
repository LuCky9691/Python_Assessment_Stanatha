#program to remove duplicates in a sorted array

def remove_duplicates(sorted_array):
    return list(dict.fromkeys(sorted_array))

sorted_array = [1, 2, 2, 3, 3, 4, 5, 5]
print(remove_duplicates(sorted_array))
