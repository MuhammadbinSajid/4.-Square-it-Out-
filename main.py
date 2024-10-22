# Get the range input from the user
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

# Create a list of square values
squares = [i**2 for i in range(start_range, end_range+1)]

# Separate the squares into odd and even values
even_squares = [square for square in squares if square % 2 == 0]
odd_squares = [square for square in squares if square % 2 != 0]

# Output the results
print("All squares:", squares)
print("Even squares:", even_squares)
print("Odd squares:", odd_squares)