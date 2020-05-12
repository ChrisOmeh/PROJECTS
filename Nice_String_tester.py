import unittest

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


# CONDITION 1
def condition_1(arg):
    """
    CONDITION 1: Doesn't contain bu, ba or be
    :param arg:
    :return:
    """
    if 'be' not in arg and 'ba' not in arg and 'bu' not in arg:
        return True
    else:
        return False


# CONDITION 2
def condition_2(arg):
    """
    CONDITION 2: It contains at least 3 vowels out of 5(a,e,i,o,u) like 'aei'.
    :param arg:
    :return:
    """
    vowel = "aeiou"
    count = 0
    for letters in arg:
        if letters in vowel:
            count += 1
            if count >= 3:
                return True
    else:
        return False


# CONDITION 3
def condition_3(arg):
    """
    CONDITION 3: It contains a double letter(At least 2 similar letters
    following each other like b in "abba".
    :param arg:
    :return:
    """
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for letters in alphabets:
        sub_string = letters * 2
        if sub_string in arg:
            return True
    else:
        return False


# THE NICE STRING FUNCTION THAT IS BASED ON THE CONDITION
def nice_string(arg):
    """
    This is the function that calls all other functions with there conditions,
    following at least 2 conditions satisfied to return True else return False
    :param arg:
    :return:
    """
    if condition_1(arg) and condition_2(arg):  # Condition 1 and 2 check
        return True
    elif condition_1(arg) and condition_3(arg):  # Condition 1 and 3 check
        return True
    elif condition_2(arg) and condition_3(arg):  # Condition 2 and 3 check
        return True
    else:
        return False


class MyTestCase(unittest.TestCase):  # Unittest of the of the nice_string algorithm

    def setUp(self):
        pass

    # Return OK if every test is passed
    def test_string(self):
        result = nice_string("bac")
        self.assertEqual(result, False)

    def test_string1(self):
        result1 = nice_string("aza")
        self.assertEqual(result1, False)

    def test_string2(self):
        result2 = nice_string("abaca")
        self.assertEqual(result2, False)

    def test_string3(self):
        result3 = nice_string("baaa")
        self.assertEqual(result3, True)

    def test_string4(self):
        result4 = nice_string("aaab")
        self.assertEqual(result4, True)

    def test_string5(self):
        result5 = nice_string("geaa")
        self.assertEqual(result5, True)

    def test_string6(self):
        result6 = nice_string("ynzz")
        self.assertEqual(result6, True)

    def test_string7(self):
        result7 = nice_string("ijao")
        self.assertEqual(result7, True)

    def test_string8(self):
        result8 = nice_string("nn")
        self.assertEqual(result8, True)

    def test_string9(self):
        result9 = nice_string("zuu")
        self.assertEqual(result9, True)

    def test_string10(self):
        result10 = nice_string("uaa")
        self.assertEqual(result10, True)

    def test_string11(self):
        result11 = nice_string("upui")
        self.assertEqual(result11, True)

    def test_string12(self):
        result12 = nice_string("oouh")
        self.assertEqual(result12, True)

    def test_string13(self):
        result13 = nice_string("wddf")
        self.assertEqual(result13, True)

    def test_string14(self):
        result14 = nice_string("baii")
        self.assertEqual(result14, True)

    def test_string15(self):
        result15 = nice_string("obee")
        self.assertEqual(result15, True)

    def test_string16(self):
        result16 = nice_string("beiuu")
        self.assertEqual(result16, True)

    def test_string17(self):
        result17 = nice_string("uyyxqptkvbtz")
        self.assertEqual(result17, True)

    def test_string18(self):
        result18 = nice_string("limseelx")
        self.assertEqual(result18, True)

    def test_string19(self):
        result19 = nice_string("zwhueqe")
        self.assertEqual(result19, True)

    def test_string20(self):
        result20 = nice_string("iwuvevd")
        self.assertEqual(result20, True)

    def test_string21(self):
        result21 = nice_string("qcdpogyeti")
        self.assertEqual(result21, True)

    def test_string22(self):
        result22 = nice_string("ygmuuyuj")
        self.assertEqual(result22, True)

    def test_string23(self):
        result23 = nice_string("cuimjyyakh")
        self.assertEqual(result23, True)

    def test_string24(self):
        result24 = nice_string("eufalmmwwbnid")
        self.assertEqual(result24, True)

    def test_string25(self):
        result25 = nice_string("kbzstzwhjeestb")
        self.assertEqual(result25, True)

    def test_string26(self):
        result26 = nice_string("rdfieknqrwxx")
        self.assertEqual(result26, True)

    def test_string27(self):
        result27 = nice_string("mzhevzkmmz")
        self.assertEqual(result27, True)

    def test_string28(self):
        result28 = nice_string("mzhevzkmmz")
        self.assertEqual(result28, True)

    def test_string29(self):
        result29 = nice_string("jootdvhbesdns")
        self.assertEqual(result29, True)

    def test_string30(self):
        result30 = nice_string("crncuotgburrcv")
        self.assertEqual(result30, True)

    def test_string31(self):
        result31 = nice_string("burppqqeivsrw")
        self.assertEqual(result31, True)

    def test_string32(self):
        result32 = nice_string("")
        self.assertEqual(result32, False)

    def test_string33(self):
        result33 = nice_string("hfrcnykh")
        self.assertEqual(result33, False)

    def test_string34(self):
        result34 = nice_string("qc")
        self.assertEqual(result34, False)

    def test_string35(self):
        result35 = nice_string("ymsetecw")
        self.assertEqual(result35, False)

    def test_string36(self):
        result36 = nice_string("bei")
        self.assertEqual(result36, False)

    def test_string37(self):
        result37 = nice_string("mbalqw")
        self.assertEqual(result37, False)

    def test_string38(self):
        result38 = nice_string("bekqe")
        self.assertEqual(result38, False)

    def test_string39(self):
        result39 = nice_string("luosbaqzdh")
        self.assertEqual(result39, False)

    def test_string40(self):
        result40 = nice_string("zcgsdbuxeo")
        self.assertEqual(result40, False)

    def test_string41(self):
        result41 = nice_string("bukipcmju")
        self.assertEqual(result41, False)

    def test_string42(self):
        result42 = nice_string("sisxxjwlkbu")
        self.assertEqual(result42, False)

    def test_string43(self):
        result43 = nice_string("bawbxffum")
        self.assertEqual(result43, False)

    def test_string44(self):
        result44 = nice_string("bbau")
        self.assertEqual(result44, False)

    def test_string45(self):
        result45 = nice_string("ax")
        self.assertEqual(result45, False)

    def test_string46(self):
        result46 = nice_string("baa")
        self.assertEqual(result46, False)

    def test_string47(self):
        result47 = nice_string("aebe")
        self.assertEqual(result47, False)

    def test_string48(self):
        result48 = nice_string("bbau")
        self.assertEqual(result48, False)

    def test_string49(self):
        result49 = nice_string("uibe")
        self.assertEqual(result49, False)

    def test_string50(self):
        result50 = nice_string("srxn")
        self.assertEqual(result50, False)

    def test_string51(self):
        result51 = nice_string("wvad")
        self.assertEqual(result51, False)

    def test_string52(self):
        result52 = nice_string("abaca")
        self.assertEqual(result52, False)

    def test_string53(self):
        result53 = nice_string("aei")
        self.assertEqual(result53, True)

    def test_string54(self):
        result54 = nice_string('abaca')
        self.assertEqual(result54, False)


if __name__ == '__main__':
    unittest.main()
