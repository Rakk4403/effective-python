# functions

## return value

Raising exception is better than returning `None`. `None` is evaluated as False in condition statement, and it could occur error. Exception is good notifier than None.

## default param

Use default param value as `None`. If you use dict or smth, they initiate only once at first. It would be very different result.