# A＠B = (A+B)×(A-B)
# n, m 입력받고
# 함수 정의하고

def plus():
    n, m = list(map(int, input().split()))
    result = (n+m)*(n-m)
    return result

answer = plus()
print(answer)
