

def cancellation(list, stop_word):
    output_list = []
    for x in list:
        if x == stop_word:
            break
        output_list.append(x)
    return output_list


    pass

def copy_all_but_skip_word(input_list, skip_word):
    output_list = []
    for element in input_list:
        if element != skip_word:
            output_list.append(element)
    return output_list

    pass

def my_average(input_list):
    total = sum(input_list)
    average = total / len(input_list)
    return average

    pass

