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
    running_values = []
    for val in list_inputs:
        if val:
           running_val += int(val)
        else: 
            running_val = 0
        if running_val > highest_value:
            highest_value = running_val
            running_values.append(highest_value)
    return running_values

def calculate_higher_value_in_list(vals_list: list):
    return sorted(vals_list, reverse=True)[0:3]

if __name__ == "__main__":
    list_inputs = open_file()
    values = add_inputs(list_inputs)
    print(calculate_higher_value_in_list(values))
