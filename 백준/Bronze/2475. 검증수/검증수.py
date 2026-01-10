n = list(map(int, input().split()))
total_sum = 0

for i in n:
    total_sum += i*i

print(total_sum % 10)