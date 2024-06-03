# Method based on lambda function
import itertools
n = int(input("Enter value n: "))
variables = [1, 2]
combinations = itertools.chain.from_iterable(itertools.product(variables, repeat=r) for r in range(1, n+1))
# Filtering combinations whose sum is n
filtered_combinations = filter(lambda combination: sum(combination) == n, combinations)
count = 0
for combination in filtered_combinations:
    count += 1
    print(f"{''.join(map(str, combination))} ({'+'.join(map(str, combination))} = {n})")
print("Number of combinations:", count)
