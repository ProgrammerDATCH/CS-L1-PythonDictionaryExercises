def string_length_dict(string_list):
    return {s: len(s) for s in string_list}

input_list = ["apple", "banana", "cherry"]
result = string_length_dict(input_list)
print(result) 
