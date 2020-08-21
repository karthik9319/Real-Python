def factorial(num: int) -> int:
    
    if not isinstance(num, int):
        return TypeError("Sorry num must be integer")
    if not num >=0:
        return ValueError("Sorry must be positive integer")
    
    def factorial_inner(num: int) -> int:
        if num <= 1:
            return 1
        return num * factorial_inner(num - 1) 
    return factorial_inner(num)

print(factorial(5))
            