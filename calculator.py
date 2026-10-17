 
CONTRIBUTORS = ["Mohamad Salaheddin"] # Conflicts generator 1
CONTRIBUTORS = ['charbel',"Sanya"] # Conflicts generator 1
 
def add(a, b):
    return a + b
 
def subtract(a, b):
    return a - b
 
def multiply(a, b):
    return a*b
 
def divide(a, b):
    pass
 
if __name__ == "__main__":
    print(f"Welcome to the Group Calculator!, written by {CONTRIBUTORS}")
    print(substract(2,2)) # Conflicts generator 2
    print(subtract(5, 2)) # Conflicts generator 2
