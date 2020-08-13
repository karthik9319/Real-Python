from decorator import do_twice

@do_twice
def say_whee():
    print("say whee")
    

@do_twice
def greet(name):
    print(f"hello {name}")

if __name__ == "__main__":
    say_whee()
    greet(name = "Karthik")