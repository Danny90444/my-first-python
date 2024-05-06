def fibn():
    if 1 > 0:
        print(1)
        
fibn()



def fib(fib1, fib2):
    count = 2
    while count <= 10:
        newfib = fib1 + fib2
        print(newfib)
        fib1 = fib2 
        fib2 = newfib
        count += 1
fib(0,1)

def fib(n):
    finalfib = 0
    if n > 1:
        finalfib = (n-1) + (n -2)
    print(finalfib)
    print((n-1))
    print((n-2))
fib(10)