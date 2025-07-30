from arithmetic_operations import perform_operation

# List of test cases (num1, num2, operation)
test_cases = [
    (5, 3, 'add'),
    (10, 4, 'subtract'),
    (6, 7, 'multiply'),
    (8, 2, 'divide'),
    (9, 0, 'divide'),
    (2, 5, 'modulus')  # invalid operation
]

# Run and print results
for num1, num2, operation in test_cases:
    result = perform_operation(num1, num2, operation)
    print(result)

