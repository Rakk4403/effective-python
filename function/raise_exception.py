def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return None


def divide_exception(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        raise ValueError('Invalid inputs')


x, y = 5, 0

print('Returning None case:')
result = divide(x, y)
if result:
    print('success: {}'.format(result))
elif not result:
    print('Invalid inputs')  # should not reach here


print('Exception case:')
try:
    result = divide_exception(x, y)
except ValueError:
    print('Invalid inputs')  # reach here
else:
    print('Result is %.1f' % result)
