def lcomb(ary, n):
    if n == 0:
        return [[]]
    if len(ary) == n:
        return [ary]
    return lcomb(ary[:-1], n) + list(map(lambda x: x + [ary[-1]], lcomb(ary[:-1], n -1)))

sum = int(input())
number = []
for i in range(1, sum+1):
    number.append(i)

print(lcomb(number, 2))

sum,    #5, 0
sum-1, sum - (sum-1)   #4, 1
sum-2, sum - (sum-2)   #3, 2
sum-3, sum - (sum-3)   #2, 3
sum-4, sum - (sum-4)   #1, 4

