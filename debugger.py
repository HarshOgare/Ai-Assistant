code = open("test.py").read()

if "print(x)" in code:
    print("Error: x is not defined")
    print("Fix: define x before using it")
