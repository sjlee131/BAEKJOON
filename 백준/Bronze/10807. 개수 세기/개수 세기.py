N = int(input())

while(True):
    a = input().split()
    list = a
    if(len(list) == N):
        break

b = input()
print(list.count(b))