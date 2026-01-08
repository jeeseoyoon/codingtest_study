# 오오.. 잘 모르겠는 문제
# 일단 n, m 받고
# 최대공약수는 둘 중 작은수 min(n,m) 으로 구해서 거기부터 냅다 나눠보기
# 최소공배수는 ... 공식이있다네
# n*m//gcd

n, m = map(int, input().split())
small = min(n,m)

for i in range(small, 0, -1):
    if n%i==0 and m%i==0:
        gcd = i
        break

lcm = n*m//gcd

print(gcd)
print(lcm)