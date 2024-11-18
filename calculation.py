
numbers = [10, 20, 30, 40, 50]

# 1. Addition
total_sum = sum(numbers)
print(f"Addition (Sum): {total_sum}")

# 2. Subtraction 
subtraction = numbers[0]
for num in numbers[1:]:
    subtraction -= num
print(f"Subtraction: {subtraction}")

# 3. Multiplication
multiplication = 1
for num in numbers:
    multiplication *= num
print(f"Multiplication: {multiplication}")

# 4. Division
division = numbers[0]
for num in numbers[1:]:
    if num != 0:  
        division /= num
print(f"Division: {division}")

# 5. Average
average = total_sum / len(numbers) if len(numbers) > 0 else 0
print(f"Average: {average}")
