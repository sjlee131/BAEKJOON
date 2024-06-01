N = int(input())

list = []

for a in range(1, N+1):
    for b in range(1):
        a, b = map(int, input().split())
        c = a + b
    list.append(c)

for numbers in list:
    print(numbers)