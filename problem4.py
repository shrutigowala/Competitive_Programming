n = int(input())
arr = list(map(int, input().split()))
target = int(input())

seen = {}

for i in range(n):
    target = target - arr[i]

    if target in seen:
        print([seen[target], i])
        break

    seen[arr[i]] = i
