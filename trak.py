def func2(arg17, arg18):
    var23 = func3(arg18, arg17)
    var85 = func4(arg17, arg18)
    result = arg18 ^ var23 & 721 & var85 & (arg18 - arg18)
    return result
def func6(arg26, arg27):
    var32 = func7(arg27, arg26)
    var62 = var35(arg27, var32)
    var66 = func11(var62, var32)
    var67 = var62 | (arg27 + var66) & var32
    var68 = var32 - var62 | -1169936125 & var67
    var69 = var68 - var67
    var70 = 1211527655 - -519
    var71 = ((var70 + 371769827) - arg27) & var62
    var72 = arg26 - arg27
    var73 = (33971403 ^ (arg27 | var71)) ^ arg27
    var74 = ((arg27 + var73) - var71) + var66
    var75 = arg26 - var69 - (var74 & var66)
    var76 = var75 | (var72 | arg26)
    var77 = var73 & var69
    var78 = 630 + var66 | var70 ^ var62
    var79 = var74 - (var62 ^ var71) ^ var69
    var80 = (var71 + var71) ^ var76 + var73
    var81 = var78 ^ var71
    var82 = (1131239774 & var66 | var69) & var76
    var83 = (var74 + arg27) ^ (var67 ^ var70)
    result = var78 | var66 - var82
    return result
def func11(arg63, arg64):
    var65 = arg63 & arg64 ^ (676 ^ (((-348 + arg63) ^ ((-509 | arg64) - 311 ^ (arg64 + (1552268065 & ((175 | -1524738318) - 162)))) | arg63 & -412 & arg63 & 62) | 1891233386) - -126)
    result = (-446402020 - -863 & -1870359692 - arg64) & (((arg63 | -654098817 + (var65 ^ arg63 & -202505561 - var65)) & 169) - 1189622381)
    return result
def func10(arg36, arg37):
    var38 = 512 - ((1885138947 & arg37) | -299)
    var39 = -1143435439 - (arg37 ^ var38 & 228)
    if var39 < var38:
        var40 = arg36 & arg37
    else:
        var40 = (var38 & var39 + -395) | arg37
    var41 = var38 | -233
    var42 = -1458652810 + var41
    var43 = arg36 | (var38 ^ var39) + 680
    var44 = (arg37 & arg37) - var41
    var45 = var43 + 127 | -1725482239 ^ 1292711825
    var46 = (arg36 - var45 - arg37) & var41
    var47 = var43 & var46
    var48 = (var39 | var41) & -1746553561
    var49 = (var47 | var43 | var48) - -695699495
    var50 = var39 - var49 - var43 & arg37
    var51 = (var43 ^ var46) + var42
    var52 = var45 | (var45 & (var43 & -902009877))
    var53 = var51 & var48
    var54 = (var46 | var51) & arg36 ^ var41
    var55 = 662 + var42 | var49
    var56 = var48 + var39
    var57 = var51 | var41
    var58 = ((var44 | var46) ^ var54) ^ var52
    var59 = arg37 | ((arg36 | var57) ^ var38)
    var60 = var41 - var41
    if var48 < arg37:
        var61 = var56 ^ var55 ^ var53 | var43
    else:
        var61 = var53 ^ var57 + var51 & var47
    result = var60 - var57
    return result
def func9():
    closure = [7]
    def func8(arg33, arg34):
        closure[0] += func10(arg33, arg34)
        return closure[0]
    func = func8
    return func
var35 = func9()
def func7(arg28, arg29):
    var30 = 0
    for var31 in range(42):
        var30 += arg28 & arg28 & arg28
    return var30
def func3(arg19, arg20):
    var21 = 0
    for var22 in range(29):
        var21 += arg19 + 8
    return var21
def func1(arg1, arg2):
    var3 = -1127652512 + -190929665 + arg2 | arg1
    var4 = arg2 ^ ((arg2 - arg2) ^ var3)
    var5 = arg1 | arg1 + arg1
    var6 = 479 ^ arg2
    var7 = var6 & (var5 + (var5 | arg1))
    var8 = var4 ^ var6
    var9 = var6 & var6 - var4
    var10 = arg1 - var9
    var11 = var10 & var8 | 16 - var9
    var12 = -1217366465 ^ var11
    var13 = arg1 + var4
    var14 = arg2 & arg1
    var15 = var10 ^ var9
    var16 = var8 | var12
    result = (var7 ^ (var9 + (343 + var9))) | (((393994009 + var6 - var15 & 580 ^ var7) - var15) | var9 - var16)
    return result
def func4(arg24, arg25):
    def func5(acc, rest):
        var84 = func6(acc, -5)
        if acc == 0:
            return var84
        else:
            result = func5(acc - 1, var84)
            return result
    result = func5(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 0'
    print 'func_number: 2'
    print 'arg_number: 17'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
    print 'prog_size: 5'
    print 'func_number: 12'
    print 'arg_number: 86'
    for i in xrange(25000):
        x = 5
        x = func2(x, i)
        print x,
