def prime(n): 
    num = 2  
    yield num
    num += 1
    count = 1
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1
    

def is_prime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

print(*prime(5))