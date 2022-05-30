# print("hello")
# print("hello world")
def isprime(n):
    if n> 1:
        for i in range(2,int(n/2)+1):
            if n%i==0:
                return False
        return True
    else:
        return False

n = int(input())
print(isprime(n))