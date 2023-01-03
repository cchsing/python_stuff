def lambdaMap(arr):

    def myfunc(arr):
        for num in arr:
            if num <= 0:
                arr.remove(num)
        for num in arr:
            index = arr.index(num)
            num2 = num ** 2
            arr[index] = num2
        return arr

    ans = map(

        # Complete the lambda function below.  It begins in the non-alterable code above
        myfunc, arr)
    return ans


if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    ans = lambdaMap(arr)
    for row in ans:
        print(' '.join(map(str, row)))
