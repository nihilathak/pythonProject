def roll_dice(size):
    return random.randint(1, size)

def math_add(var1, var2):
    return var1 + var2
    #print("result:" + var3)

def math_sub(var1, var2):
    return var1 + var2
    #print("result:" + var3)

def math_mult(var1, var2):
    return var1 * var2

def math_div(var1, var2):
    return var1 / var2

def exp (base, pow):
    return base**pow

def exp_loop(base, pow):
    result = 1
    for index in range(pow):
        result = result * base
