def seqSearch(data, target):
    for i in range(len(data)):
        if target == data[i]:
            return i
    return -1


if __name__ == '__main__':
    ret = seqSearch([1,2,3,34,56,57,78,87],57)
    print(f'ret index is: {ret}')