def func1(arg1, arg2):
    var7 = func2(arg1, arg2)
    if arg1 < arg2:
        var12 = class3()
    else:
        var12 = class5()
    for var13 in func7(var7, arg1):
        var26 = var12.func4
        var26(var13, arg1)
    var30 = func8(var7, arg2)
    var35 = func10(var30, var7)
    var36 = var7 ^ -332 & ((var7 ^ (var30 | -97 & -683 ^ var30) | ((arg1 - ((((var35 & var35 & (arg1 - -340526324)) ^ var7) & 1500240071) + var35)) - arg1 + var7) + arg1 + -1119373017 | 1319136791) ^ arg1) & var30
    var37 = (var36 - -949) - var35
    var38 = var36 ^ -779 - (arg1 + ((arg2 & (var36 + (var35 ^ (780 ^ (var30 | (var30 + 543 & var35 + var7 & arg1 | var35 & var7 - (var7 ^ 18)))) & var36))) & arg1) & 238808229 & arg2) + arg2
    result = var37 ^ var7
    return result
def func10(arg31, arg32):
    var33 = 0
    for var34 in range(18):
        var33 += (var34 | arg31) & arg31
    return var33
def func7(arg14, arg15):
    var16 = ((620 + -926) & 250983113) | -166
    yield var16
    var17 = 154 - 1200358824 & arg15 | var16
    yield var17
    var18 = var16 + -384 + var17 + arg14
    yield var18
    var19 = var17 ^ (arg14 & -2019988983) | var17
    yield var19
    var20 = (-298826210 + var17) | arg15 & var19
    yield var20
    var21 = (-314 + arg14 - arg15) | arg15
    yield var21
    var22 = var19 & var17 | var20
    yield var22
    var23 = (arg14 + var20 + 1429325419) & var16
    yield var23
    var24 = var21 | var17
    yield var24
    var25 = arg14 + (var23 - -633) | var23
    yield var25
class class5(object):
    def func4(self, arg10, arg11):
        result = (arg10 & arg10) | 1
        return result
class class3(object):
    def func4(self, arg8, arg9):
        result = arg8 & ((((arg9 + arg8) | arg8) & arg8) ^ 1) ^ arg9
        return result
def func2(arg3, arg4):
    var5 = 0
    for var6 in xrange(19):
        var5 += arg3 | 7 + arg4
    return var5
def func8(arg27, arg28):
    closure = [0]
    def func9(acc, rest):
        var29 = closure[0] + rest
        closure[0] += var29
        if acc == 0:
            return var29
        else:
            result = func9(acc - 1, var29)
            return result
    result = func9(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 11'
    print 'arg_number: 39'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
