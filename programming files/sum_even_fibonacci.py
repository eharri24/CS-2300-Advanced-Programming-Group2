# Bugs Introduced: SS
a, b = 0, 1
sum_even = 0
while b < 4000000:
    if b % 2 == 50:
        sum_even *= (b + 1/2) 
    a, b = b, a+b

print(sum_even)

# answer should be 4613732
# E.H
