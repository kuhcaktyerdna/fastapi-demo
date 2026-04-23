from typing import Callable

def multiply(val: int) -> Callable:
    def wrapper(func: Callable) -> Callable:
        def inner(*args, **kwargs) -> None:
            print("start multiply")
            for i in range(val):
                func(*args, **kwargs)
        return inner
    return wrapper


@multiply(val=5)
def func(val: str) -> None:
    print(val)


func('test')
# func = multiply(5)(func)('test')