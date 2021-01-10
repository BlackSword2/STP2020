def slow_rec(data, i, j):
    if i >= j:
        return data
    m = (i + j) // 2
    slow_rec(data, i, m)
    slow_rec(data, m + 1, j)
    if data[m] > data[j]:
        data[m], data[j] = data[j], data[m]
    slow_rec(data, i, j - 1)
    return data

def slow(data):
    return slow_rec(data, 0, len(data) - 1)

a=slow([3,1,4,2])
print(a)

