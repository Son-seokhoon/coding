a=int(input())

for i in range(a):
    x,y=map(int,input().split())
    print(f"You get {x//y} piece(s) and your dad gets {x%y} piece(s).")
