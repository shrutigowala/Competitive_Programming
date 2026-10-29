n = int(input())
arr = list(map(int, input().split()))
target = int(input())

left = 0
high = n - 1

while left <= high:
    mid = (left + high) // 2

    if arr[mid] == target:
        print(mid)
        break

    elif arr[mid] > target:
        left = mid + 1

    else:
        high = mid - 1

else:
    print(-1)
