startH, startM = map(int, input().split())
time = int(input())

endM = startM + time

if(endM >= 60):
    a = endM // 60 
    b = endM % 60
    endH = startH + a
    endM = b
else:
    endH = startH
    endM = startM + time

if(endH >= 24):
    endH = endH - 24

print(endH, endM)