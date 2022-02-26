def IsPrime(n):
    if n == 1: return False
    
    import math, random
    
    # проверка на делимость в пределах 257 делителей
    for i in range(2, min(257, math.ceil(math.sqrt(n))) ):
        if n % i == 0:
            return False
    
    # тест Миллера — Рабина
    k = max(math.ceil(math.log(n, 2)), 10)
    
    s = 0
    d = n - 1
    
    while d % 2 == 0:
        s += 1
        d //= 2
    
    for _ in range(k):
        a_k = random.randint(2, n - 2)
        x = pow(a_k, d, n)
        
        if x == 1 or x == n - 1: # проверка на первое условие
            continue
        
        flag = False
        for _ in range(s - 1): # проверка на второе условие
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                flag = True
                break
        
        if flag:
            continue
            
        return False
    return True

def GenPrimeNumber(k = 1024):
    import random
    
    bits = [random.choice([0, 1]) for _ in range(k)]
    
    bits[0], bits[-1] = 1, 1
    
    def ToNum(lst):
        k = 0
        result = 0

        for i in lst:
            result += i * (2 ** k)
            k += 1

        return result
    
    result = ToNum(bits)
    
    while not IsPrime(result):
        result += 2
        
    return result

def Inverse(e, phi_n):
    t = 0   
    newt = 1
    r = phi_n     
    newr = e

    while newr != 0:
        quotient = r // newr
        t, newt = newt, t - quotient * newt
        r, newr = newr, r - quotient * newr

    if r > 1:
        return "не обратимо"
    if t < 0:
        t = t + phi_n

    return t

def RSA(k = 1024):
    import random
    
    p = GenPrimeNumber(k)
    q = GenPrimeNumber(k)
    
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = random.choice([17, 257, 65537, GenPrimeNumber(10)])
    d = Inverse(e, phi_n)
    
    return [(e, n), (d, n)]

def Encrypt(message, open_key):
    import random
    
    lst = [random.randint(1, 1000)] + [ord(i) for i in message]
    
    a = 0
    
    for i in range(len(lst)):
        lst[i] = lst[i] + a
        a = lst[i]
    
    return [pow(i, *open_key) for i in lst]

def Decrypt(lst, secret_key):
    temp_lst = [pow(i, *secret_key) for i in lst]
    
    message = ""
    
    a = 0
    
    for i in range(len(lst)):
        message += chr(temp_lst[i] - a)
        a = temp_lst[i]
        
    return message[1:]

if __name__ == "__main__":
    open_key, secret_key = RSA()
    print(open_key)

    message = "Hellow, World!"
    en = Encrypt(message, open_key)
    Decrypt(en, secret_key)