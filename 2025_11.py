"""
Samozřejmě to jde počítat jako (2*sqrt(2025))-1, ale já mám radši programování.
"""

def find_last(number: int):
    i = 1
    while True:
        number -= i
        if number == 0:
            return i
        else:
            i += 2

print(find_last(2025))
