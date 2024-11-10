numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes=[]
not_primes=[]
for i in range(len(numbers)):
    x=0
    for j in range(len(numbers)):
        z=numbers[i]%numbers[j]
        if z==0:
            x=x+1
        if x>2:
            break
    if x>2:
        not_primes.append(numbers[i])
    else:
        if numbers[i]==1:
            continue
        primes.append(numbers[i])
print('numbers = ',numbers,'Primes = ',primes,'Not Primes = ',not_primes)