## Given balls of these three colors arranged randomly in a line (it does not matter how many
# balls there are), the task is to arrange them such that all balls of the same color are together
# and their collective color groups are in the correct order.
# Reference : https://en.wikipedia.org/wiki/Dutch_national_flag_problem

def three_way_partition(arr, mid=1):
    # red=0, white=1, blue=2, mid=white
    i = 0
    j = 0
    k = len(arr) - 1
    while j <= k:
        if arr[j] < mid:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        elif arr[j] > mid:
            arr[j], arr[k] = arr[k], arr[j]
            k -= 1
        else:
            j += 1
    return arr


if __name__ == '__main__':
    partitioned_array = three_way_partition([2,0,2,1,1,0])
    print(partitioned_array)