
# import testmod for testing our function
from doctest import testmod

def condition_1(x):
    """
    >>> condition_1('b')
    False
    """
    if 'be' not in x and 'ba' not in x and 'bu' not in x:
        return True
    else:
        return False


if __name__ == '__main__':
    testmod(name='condition_1', verbose=True)
