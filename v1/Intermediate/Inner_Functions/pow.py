def generate_power(number):
    print("here")
    def nth_power(power):
        print("here2")
        return number**power
    print("here3")
    
    def cubed():
        return number**3
    
    return nth_power

a = generate_power(2)
print(a(5))