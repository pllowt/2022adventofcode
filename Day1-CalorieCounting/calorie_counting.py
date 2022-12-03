def read_lines_in_file_to_list() -> list:
    with open('input.txt', 'r') as file:
        contents = file.read()
        list_of_inputs = []
        for word in contents.split('\n'):
            list_of_inputs.append(word.strip())
        return list_of_inputs


def split_list_on_empty_element(num_list: list) -> list:
    return [i.split() for i in num_list]
    # highest_value = 0
    # running_val = 0
    # running_values = []
    # for val in num_list:
    #     if val:
    #         running_val += int(val)
    #     else:
    #         running_values.append(highest_value)
    #         running_val = 0
    #     if running_val > highest_value:
    #         highest_value = running_val
    # return running_values


def return_largest_three_values_in_list(vals_list: list):
    return sorted(vals_list, reverse=True)[0:3]


if __name__ == "__main__":
    list_inputs = read_lines_in_file_to_list()
    values = add_int_elements_in_none_separated_list(list_inputs)
    print(sum(return_largest_three_values_in_list(values)))
