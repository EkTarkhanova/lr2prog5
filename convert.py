__all__ = ['convert_precision']

def convert_precision(precision='0.00001'):
    if isinstance(precision, float):
        precision = str(precision)

    for i, char in enumerate(precision):
        if char == '.':
            continue
        if char != '0':
            return i
    return len(precision) - precision.index('.') - 1 if '.' in precision else 0
