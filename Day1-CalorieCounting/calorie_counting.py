def open_file():
    with open('input.txt', 'r') as input:
        contents = input.read()
        list_of_inputs = []
        for word in contents.split('\n'):
            list_of_inputs.append(word.strip())
        return list_of_inputs

def add_inputs(list_inputs: list):
    highest_value = 0 
    running_val = 0
    for val in list_inputs:
        if val:
           running_val += int(val)
        else: 
            running_val = 0
        if running_val > highest_value:
            highest_value = running_val
    return highest_value

def calculate_higher_value_in_list(value: int, vals_list: list):
    for index, val in enumerate(vals_list):
        if value > val:
            vals_list[index] = value
    return vals_list

if __name__ == "__main__":
    list_inputs = open_file()
    print(add_inputs(list_inputs))
