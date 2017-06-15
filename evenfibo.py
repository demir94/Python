even, odd = 0,1
total = 0
while True:
    secondOdd = even + odd
    even = odd + secondOdd
    if even < 4000000:
        total += even
        odd = secondOdd + even
    else:
        break
print total