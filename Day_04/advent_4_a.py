def isIncreasing(x):
    num = str(x)
    for i in range(1, len(num)):
        if num[i - 1] > num[i]:
            return False
    return True

def hasSameDigits(x):
    num = str(x)
    for i in range(1, len(num)):
        if num[i - 1] == num[i]:
            return True
    return False

cntr = 0
for i in range(108457, 562041):
    if isIncreasing(i) and hasSameDigits(i):
        cntr += 1

print(cntr)
