n = int(input())

winners = []
total_wins = 0
for _ in range(n):
    name, result = input().split()
    if result == 'win':
        winners.append(name)
        total_wins += 1

print(winners)
print(total_wins)
