import math

def jumpSearch(data, target):
    n = len(data)
    step = int(math.floor(math.sqrt(n)))
    prev = 0
    while data[min(step,n)-1]<target:
        prev = step
        step = step + int(math.floor(math.sqrt(n)))
        if prev >=n:
            return -1
    while data[prev]<target:
        prev += 1
        if prev == min(step,n):
            return -1
    if data[prev] == target:
        return prev
    else:
        return -1
    

if __name__ == '__main__':
    data = [i for i in range(1,50000,2)]
    ret = jumpSearch(data,8006)
    print(f'ret index is: {ret}')