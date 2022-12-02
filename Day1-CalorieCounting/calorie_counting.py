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

if __name__ == "__main__":
    list_inputs = open_file()
    print(add_inputs(list_inputs))
