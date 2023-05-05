# Write your code below this row 👇

sum_even_numbers = 0

# Option 1
for n in range(2, 101):
    if n % 2 == 0:
        sum_even_numbers += n

# Option 2
for n in range(2, 101, 2):
    sum_even_numbers += n

print(sum_even_numbers)
