#Day 5 - floats

"""
Method imitates range() built-in function but works for floats.

Method can be improved by addressing float inaccuracy issue. 
Method does not resolve this problem at the moment.
"""

class Range:

    def range_float(start: float, stop=None, step=None):
        if step==None:
            step = 1.0
            if stop==None:
                try:
                    stop = float(start)
                    start = 0.0
                    step = 1.0
                except:
                    print("Invalid method argument.")
        try:
            start = float(start)
            stop = float(stop)
            step = float(step)
        except:
            print("Invalid method arguments.")
            return
        count = 0
        while True:
            gen = start + (step * count)
            if stop >= gen and step < 0:
                break
            if stop <= gen and step > 0:
                break
            yield gen
            count += 1

print(f'3 arguments:')
for i in Range.range_float(1.2, 6.0, 0.8):
    print(i, end='  ')

print(f'\n2 arguments:')
for i in Range.range_float(-6.4, -1.4):
    print(i, end='  ')

print(f'\n1 argument:')
for i in Range.range_float(7.4):
    print(i, end='  ')

