n = int(input())

bocals = [input() for _ in range(n)]
new_bocals = sorted(set(bocals), key=lambda d: bocals.index(d))

for bocal in new_bocals:
    print(bocal)

