import math

def pi():
    return math.pi

def addition(a, b):
    return a+b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

def minus(a, b):
    return a-b

def dividetheuniverseby(a):
    universe = math.pi*994541295248716
    return universe/a

def multiplytheuniverseby(a):
    universe = math.pi*994541295248716
    return universe*a

def additiontheuniverseby(a):
    universe = math.pi*994541295248716
    return universe+a

def theuniverseminus(a):
    universe = math.pi*994541295248716
    return universe-a

def othercalc(symbol, a, b):
    if symbol == 'cos':
        return math.cos(a)
    elif symbol == 'sin':
        return math.sin(a)
    elif symbol == 'sqrt':
        return math.sqrt(a)
    elif symbol == 'pow':
        return math.pow(a, b)
    elif symbol == 'floor':
        return math.floor(a)
    elif symbol == 'log':
        return math.log(a)
    elif symbol == 'exp':
        return math.exp(a)
    elif symbol == 'fabs':
        return math.fabs(a)
    elif symbol == 'lgamma':
        return math.lgamma(a)
    elif symbol == 'log1p':
        return math.log1p(a)
    elif symbol == 'ceil':
        return math.ceil(a)
    else:
        return None

def ihatemath():
    return 'well then dont use this module!!!1!!1!1!1!1!'

def whatismath():
    return 'https://en.wikipedia.org/wiki/Math'