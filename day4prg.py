

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    return pair(lambda a, b: a)

def cdr(pair):
    return pair(lambda a, b: b)

p = cons(3, 4)

print("car(cons(3, 4)) =", car(p))  # Output: 3
print("cdr(cons(3, 4)) =", cdr(p))  # Output: 4
