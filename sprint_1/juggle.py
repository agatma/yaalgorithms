def max_points(*, keys):
    counter = [0] * 10
    for _ in range(4):
        for value in input():
            if value != '.':
                counter[int(value)] += 1
    return sum(1 if 0 < value <= 2 * keys else 0 for value in counter)


keys = int(input())

print(max_points(keys=keys))
