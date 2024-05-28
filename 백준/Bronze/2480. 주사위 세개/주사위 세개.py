a, b, c = map(int, input().split())
list = [a, b, c]

if(a == b == c):
    score = 10000 + (a * 1000)
elif(a == b != c):
    score = 1000 + (a * 100)
elif(a == c != b):
    score = 1000 + (a * 100)
elif(a != b == c): 
    score = 1000 + (b * 100)
else:
    score = max(list) * 100
print(score)