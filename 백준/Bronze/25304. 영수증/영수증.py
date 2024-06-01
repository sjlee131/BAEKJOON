X = int(input())
N = int(input())    # 줄 수가 되어야 함.

list = []

for a in range(1, N+1):
    for b in range(1):
        a, b = map(int, input().split())
        c = a * b
        list.append(c)
        d = sum(list)

if(X == d):
    print("Yes")
else:
    print("No")