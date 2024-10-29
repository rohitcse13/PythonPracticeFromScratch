# Sum of two numbers
# Select two numbers and assign them to variables 'a' and 'b'
# Then calculate their sum and display it
a = 10
b = 20
print("a + b = ", a + b)  # Output: 30 (10 + 20)

# Difference of two numbers
# Assign values to 'a' and 'b' and calculate the difference (a - b)
# Print the result
a = 10
b = 20
print("a - b = ", a - b)  # Output: -10 (10 - 20)

# Product of two numbers
# Multiply 'a' and 'b' and display the product
a = 10
b = 20
print("a * b = ", a * b)  # Output: 200 (10 * 20)

# Division of two numbers
# Divide 'a' by 'b' and print the quotient
a = 10
b = 20
print("a / b = ", a / b)  # Output: 0.5 (10 / 20)

# Modulus of two numbers
# Calculate the remainder when 'a' is divided by 'b' using modulus operator
a = 10
b = 20
print("a % b = ", a % b)  # Output: 10 (10 % 20)

# Exponentiation
# Raise 'a' to the power of 'b' using the exponent operator (**)
a = 10
b = 2
print("a ** b = ", a ** b)  # Output: 100 (10^2)

# Floor Division
# Floor division gives the largest integer quotient (rounds down to the nearest integer)
a = 10
b = 3
print("a // b = ", a // b)  # Output: 3 (10 // 3)

# Operator Precedence
# Operators are applied in the order of precedence, where '*' has higher precedence than '+'
a = 10
b = 20
c = 30
print("a + b * c = ", a + b * c)  # Output: 610 (10 + (20 * 30))

# Changing Precedence with Parentheses
# Using parentheses to change precedence: addition occurs first, then multiplication
a = 10
b = 20
c = 30
print("(a + b) * c = ", (a + b) * c)  # Output: 900 ((10 + 20) * 30)

# Exponentiation with Addition
# Exponentiation has higher precedence than addition
a = 10
b = 2
c = 30
print("a ** b + c = ", a ** b + c)  # Output: 130 (10^20 + 3)

# Addition with Exponentiation
# Here, '**' takes precedence over '+'
a = 10
b = 20
c = 3
print("a + b ** c = ", a + b ** c)  # Output: 4010 (10 + 20^3)

# Using Parentheses to Change Exponentiation Order
# Parentheses change precedence so addition occurs first, then exponentiation
a = 10
b = 20
c = 3
print("(a + b) ** c = ", (a + b) ** c)  # Output: 27000 ((10 + 20)^3)

# Mixed Operations with Multiplication and Addition
# Multiplication has a higher precedence than addition
a = 10
b = 20
c = 30
print("a * b + c = ", a * b + c)  # Output: 230 ((10 * 20) + 30)
