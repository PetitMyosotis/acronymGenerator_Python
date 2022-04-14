import string

print("Enter something (i will give you the acronym)")
name = input()


def accro_generator(text):
    name_array = []
    name_array = name.split(" ")
    array_len = len(name_array)
    iteration = 0
    array_first_letter = []
    for i in range(array_len):
        first_letter = name_array[iteration][:1]
        array_first_letter.append(first_letter)
        iteration = iteration + 1
    array_first_letter = ''.join(array_first_letter)
    array_first_letter = array_first_letter.upper()
    return array_first_letter


result = accro_generator(name)

print(result)




