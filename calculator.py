from typing import Union

__all__ = ['calculate']


def calculate(x: Union[float, int], y: Union[float, int],
              op: str) -> Union[float, int]:
  
   
    if op == "+":
        resh = x + y
    elif op == "-":
        resh = x - y
    elif op == "*":
        resh = x * y
    elif op == "/":
        if y != 0:
            resh = x / y
        else:
            resh = "деление на 0 невозможно"
    elif op == "**":
        resh = x**y
    elif op == "%":
    
        if y != 0:
            resh = x % y
        else:
            resh = "деление на 0 невозможно"
    else:
        resh = "неизвестная операция"

    return resh


