import sys

stack = []

for x in sys.argv:#Input parser puts all of string on stack. each value is either a operator or a number
    n = x.replace("'", '')
    n=n.replace('(', '')
    n=n.replace(')', '')
    i = len(n)
    if i==1:
        stack.append(n)

cache = []#cache keeps track of already processed information
while len(stack) > 1 or len(cache) > 1:
    inp = stack.pop()
    if inp == "+" or inp == "-" or inp == "*" or inp == "/":#operators will never be after less than 2 numbers
        n1 = cache.pop()
        n2 = cache.pop()
        if inp == "+":
            stack.append(n1+n2)
        elif inp == "-":
            stack.append(n1-n2)
        elif inp == "*":
            stack.append(n1*n2)
        else:
            stack.append(n1/n2)
    else:
        cache.append(int(inp))

print(stack.pop())