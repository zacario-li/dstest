def binSearch(data, target):
    low = 0
    high = len(data)-1
    cycle = 0
    while low <= high:
        cycle += 1
        print(f'cycle: {cycle}')
        mid = int((low + high)/2)
        if data[mid] < target:
            low = mid + 1
        elif data[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1

if __name__ == '__main__':
    ret = binSearch([1,2,3,34,56,57,78,87],57)
    print(f'ret index is: {ret}')