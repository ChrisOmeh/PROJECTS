# CONDITION 1
def condition_1(x):
    if 'be' not in x and 'ba' not in x and 'bu' not in x:
        return True
    else:
        return False


print(condition_1(' aei'))


# CONDITION 2
def condition_2(x):
    if 'a' * 3 in x or 'e' * 3 in x or 'i' * 3 in x or 'o' * 3 in x or 'u' * 3 in x:
        return True
    else:
        return False


print(condition_2('wedcu'))


# CONDITION 3
def condition_3(x):
    if 'aa' in x or 'bb' in x or 'cc' in x or 'dd' in x or 'ee' in x or 'ff' in x:
        return True
    if 'gg' in x or 'hh' in x or 'ii' in x or 'jj' in x or 'kk' in x or 'll' in x:
        return True
    if 'mm' in x or 'nn' in x or 'oo' in x or 'pp' in x or 'rr' in x or 'ss' in x:
        return True
    if 'tt' in x or 'uu' in x or 'vv' in x or 'ww' in x or 'xx' in x or 'yy' in x or 'zz' in x:
        return True
    else:
        return False


print(condition_3('w'))
