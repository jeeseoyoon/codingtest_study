# 테스트 케이스 받고
# k층 n호 받고..
# 1-n까지 리스트 만들기 그리고 k층까지 반복..?
# 리스트에서 맨 앞부터 끝까지 더하기
# 현재 = 아랫집 전체 값 + 내 층 왼쪽부터 누적 값
# 반복 다하면 마지막호 출력.. 근데 0부터 시작하니까 -1 해야돼

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    people = [i for i in range(1, n + 1)]
    
    for _ in range(k):
        for i in range(1, n):
            people[i] += people[i-1]

    print(people[-1])