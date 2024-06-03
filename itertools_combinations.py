# A method that uses the `itertools` library to generate combinations of numbers
import itertools
n = int(input("Enter value n: "))
variables = [1, 2]
count = 0
for r in range(1, n+1):
    for combination in itertools.product(variables, repeat=r):
        if sum(combination) == n:
            count += 1
            print(f"{''.join(map(str, combination))} ({'+'.join(map(str, combination))} = {n})")
print("Number of combinations:", count)
