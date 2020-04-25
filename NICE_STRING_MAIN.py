"""
TASK STATEMENT
-A string is nice if at least 2 out the 3 conditions are obeyed.
-Doesn't contain substring 'ba','bu' or 'be'.
-It contains at least 3 vowels out of 5(a,e,i,o,u) like 'aei'.
-It contains a double letter(At least 2 similar letters following
 each other like b in "abba".

INPUT STATEMENT
This Nice String Algorithm takes a string argument. The string argument is
tested under certain conditions commented as CONDITION 1, CONDITION 2 and
CONDITION 3. NOTE: STRING ARGUMENTS MUST BE IN LOWER CASES ONLY. THOUGH, THE
ALGORITHM HAVE THE ABILITY TO CONVERT ANY UPPER CASE TO LOWER CASE AT RUNTIME.

OUTPUT STATEMENT
The output of this algorithm is what is termed NICE STRING. Nice string in the
sense that at least two(2) out of the three(3) conditions are satisfied. If any
of these two(2) conditions are satisfied, the algorithm returns TRUE; ELse it
returns FALSE.
"""


class NiceString:
    def __init__(self, x):
        self.x = x

    # CONDITION 1
    def condition_1(self, x):
        """
        CONDITION 1: Doesn't contain bu, ba or be
        :param x:
        :return:
        """
        if 'be' not in x and 'ba' not in x and 'bu' not in x:
            return True
        else:
            return False

    # CONDITION 2

    def condition_2(self, x):
        """
        CONDITION 2: It contains at least 3 vowels out of 5(a,e,i,o,u) like 'aei'.
        :param x:
        :return:
        """
        main_list = []
        from itertools import permutations
        substring1_in = list(permutations('aeiou', 3))
        for i in substring1_in:
            s = "".join(i)
            main_list.append(s)
        if 'a' * 3 in x or 'e' * 3 in x or 'i' * 3 in x or 'o' * 3 in x or 'u' * 3 in x:
            return True
        for letter in main_list:
            if letter in x:
                return True
        else:
            return False

    # CONDITION 3
    def condition_3(self, x):
        """
        CONDITION 3: It contains a double letter(At least 2 similar letters
        following each other like b in "abba".
        :param x:
        :return:
        """
        if 'aa' in x or 'bb' in x or 'cc' in x or 'dd' in x or 'ee' in x or 'ff' in x:
            return True
        if 'gg' in x or 'hh' in x or 'ii' in x or 'jj' in x or 'kk' in x or 'll' in x:
            return True
        if 'mm' in x or 'nn' in x or 'oo' in x or 'pp' in x or 'qq' in x or 'rr' in x or 'ss' in x:
            return True
        if 'tt' in x or 'uu' in x or 'vv' in x or 'ww' in x or 'xx' in x or 'yy' in x or 'zz' in x:
            return True
        else:
            return False

    # THE NICE STRING FUNCTION THAT IS BASED ON THE CONDITION
    def nice_string(self, x):
        """
        This is the function that calls all other functions with there conditions,
        following at least 2 conditions satisfied to return True else return False
        :param x:
        :return:
        """
        if self.condition_1(x) and self.condition_2(x):
            return True, 'Is a nice string'
        if self.condition_1(x) and self.condition_3(x):
            return True, 'Is a nice string'
        if self.condition_2(x) and self.condition_3(x):
            return True, 'Is a nice string'
        else:
            return False, 'Is not a nice string'


Final_result = NiceString(x=''.lower())
print(Final_result.nice_string('Remove me to enter the string argument'.lower()))

# REMOVE THE COMMAND INSIDE THE .nice_string()
# enter your choice string argument before the (.)
# Don't remove the single inverted comma while entering string, enter your string
# inside the inverted comma.'enter string here'
