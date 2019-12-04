def isIncreasing(x):
    num = str(x)
    for i in range(1, len(num)):
        if num[i - 1] > num[i]:
            return False
    return True

def hasSameDigits(x):
    num = str(x)
    grp_cntr = 1
    for i in range(1, len(num)):
        if num[i - 1] == num[i]:
            grp_cntr += 1
        else:
            if grp_cntr == 2:
                return True
            grp_cntr = 1
    return grp_cntr == 2

cntr = 0
for i in range(108457, 562041):
    if isIncreasing(i) and hasSameDigits(i):
        cntr += 1

print(cntr)
