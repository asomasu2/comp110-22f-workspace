"""An example function definition"""

def my_max(a: int, b: int) -> int:
    """Returns the largest argument."""
    if a >= b:
        return a
    else: 
        return b
 
print(my_max(11,10))

def hello_n(n: int) -> int:
   """A silly example function."""
   return "hello " + str(n)

print(hello_n(3))