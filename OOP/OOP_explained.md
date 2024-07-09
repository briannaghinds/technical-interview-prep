# Object Oriented Programming

### Conceptual Understanding Explanations:
(1) **Explain the core principles of OOP. Briefly dicuss inheritance, encapsulation, polymorphism, and abstraction.**

(2) **Differentiate between Procedural Programming and OOP. Explain how the approach problem-solving and data organization.**

(3) **Describe the advantages and disadvantages of using OOP in Python.**

### Classes and Objects
(within class_obj.py, snapshots will be in here also)
(1) **Design a class representing a bank account. Include attributes like balance, account holder, and methods for deposit, withdrawal, and displaying balance.**

```python
# skeleton
class BankAccount:
    def __init__(self, balance:int, account_holder:str):
        self.balance = balance
        self.account_holder = account_holder

    # getter for balance
    def getBalance(self):
        return self.balance
    
    def deposit(self, amount):
        pass

    def withdrawal(self, amount):
        pass

    def display_balance(self):
        pass
```

(2) **Explain the concept of a constructor (the __init__() method) and its role in object creation.**

(3) **Describe the difference between instance methods, class methods, and static methods in Python. Provide an example for each.**

### Inheritance
(within inheritance.py)
(1) **Create a class hierarchy for different shapes (e.g., Square, Circle) with a base class named Shape. Define common methods like get_area() in the base class and override them in specific shapes.**

(2) **Explain the concept of method overriding and method overloading in Python with an inheritance example.**

(3) **Describe how you can achieve data hiding in Python classes even without private access modifiers.**

### Polymorphism
(within polymorphisn.py)
(1) **Implement a function draw_shape(shape) that takes a Shape object as input and calls its specific draw() method based on the object type (achieved through polymorphism).**

(2) **Explain Duck Typing and its role in achieving polymorphism in Python.**

(3) **Discuss the difference between operator overloading and method overriding.**