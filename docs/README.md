# Python use cases and records

## Exceptions Handling

1. try, except, raise, else, assert, finally

```
# program to print the reciprocal of even numbers
try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)
finally:
    print("This is finally block")
```

2. `"assert condition, message"` is equivalent to

```
if **debug**:
if not condition:
raise AssertionError(message)

```
