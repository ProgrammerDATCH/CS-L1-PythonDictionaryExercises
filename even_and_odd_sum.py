def sum_even_odd(numbers):
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    return (even_sum, odd_sum)

# Example usage:
input_list = [1, 2, 3, 4, 5, 6]
result = sum_even_odd(input_list)
print(result)
