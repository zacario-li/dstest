def insertSearch(data, target):
    low = 0
    high = len(data)-1
    while low<=high:
        mid = low + (target-data[low])//(target-data[low])*(high - low)
        if target > data[mid]:
            low = mid + 1
        elif target < data[mid]:
            high = mid - 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    ret = insertSearch([1,2,3,34,56,57,78,87],57)
    print(f'ret index is: {ret}')