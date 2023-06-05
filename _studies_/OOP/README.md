# Object-Oriented Programming with Python

This repository contains a comprehensive guide to Object-Oriented Programming (OOP) using Python. In this guide, we will explore the concepts of classes and methods, and learn how to utilize them effectively in Python.

## Table of Contents

- [Introduction to OOP](#introduction-to-oop)
- [Classes](#classes)
- [Methods](#methods)
- [Inheritance](#inheritance)
- [Polymorphism](#polymorphism)
- [Encapsulation](#encapsulation)
- [Abstraction](#abstraction)
- [Conclusion](#conclusion)

## Introduction to OOP

Object-Oriented Programming is a programming paradigm that focuses on creating objects, which are instances of classes, to represent real-world entities and provide a modular and organized approach to software development. It emphasizes the concepts of encapsulation, inheritance, polymorphism, and abstraction.

Python is a powerful and versatile programming language that fully supports OOP. With Python's built-in features, we can create classes, define methods, and utilize inheritance to build complex and scalable applications.

In this guide, we will explore various aspects of OOP in Python, from creating classes to implementing inheritance and polymorphism.

## Classes

A class is a blueprint for creating objects that define their properties (attributes) and behavior (methods). It serves as a template for creating instances of objects. In Python, a class is defined using the `class` keyword.

Here's an example of a simple class in Python:

```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print("Engine started!")

    def drive(self, distance):
        print(f"The {self.brand} {self.model} has driven {distance} miles.")

car1 = Car("Toyota", "Camry", 2022)
car1.start_engine()
car1.drive(100)
```

This example demonstrates a `Car` class with attributes like `brand`, `model`, and `year`, and methods like `start_engine` and `drive`. We can create instances of this class, set their attributes, and invoke their methods.

## Methods

Methods are functions defined within a class that perform specific actions or provide functionality to the objects created from the class. They can access and modify the attributes of an object. Python provides two types of methods: instance methods and class methods.

Instance methods are defined inside a class and operate on individual instances of the class. They are called on instances and have access to the instance's attributes. The `self` parameter refers to the instance itself.

Class methods are defined using the `@classmethod` decorator and operate on the class itself rather than instances. They have access to the class attributes and can be used for various utility functions related to the class.

In the previous example, `start_engine` and `drive` are instance methods that operate on individual `Car` instances.

```python
class Car:
    # ...

    def start_engine(self):
        print("Engine started!")

    def drive(self, distance):
        print(f"The {self.brand} {self.model} has driven {distance} miles.")
```

## Inheritance

Inheritance is a mechanism in OOP that allows a class to inherit attributes and methods from another class, known as the parent or base class. The class inheriting from the parent class is called the child or derived class. Inheritance promotes code reuse and facilitates the creation of more specialized classes.

To create a child class that inherits from a parent class, we define the child class and specify the parent class in parentheses after the child class name.

```python
class

 ElectricCar(Car):
    def charge(self):
        print(f"The {self.brand} {self.model} is charging.")
```

In this example, the `ElectricCar` class inherits from the `Car` class. The `ElectricCar` class has its own `charge` method in addition to inheriting the `start_engine` and `drive` methods from the `Car` class.

## Polymorphism

Polymorphism allows objects of different classes to be treated as objects of a common base class. It enables the use of a single interface to represent different types of objects, promoting flexibility and modularity in code.

Polymorphism is achieved through method overriding and method overloading.

Method overriding allows a derived class to provide a different implementation of a method that is already defined in its parent class. The overridden method in the derived class is called instead of the parent class method when the method is invoked on objects of the derived class.

Method overloading is the ability to define multiple methods with the same name but different parameters. Python does not support explicit method overloading, but it can be achieved using default parameter values or variable arguments.

## Encapsulation

Encapsulation is the principle of bundling data (attributes) and methods that operate on that data within a class, and controlling access to the internal state of objects. It ensures that the internal representation and behavior of an object are hidden from the outside, and can only be accessed through defined interfaces (methods).

In Python, encapsulation is achieved by using access modifiers. By convention, attributes and methods prefixed with an underscore (`_`) are considered internal and should not be accessed directly from outside the class. However, this is merely a convention, as Python does not enforce strict access control.

## Abstraction

Abstraction is the process of representing complex real-world entities as simplified models within a program. It allows us to focus on essential attributes and behaviors while hiding unnecessary details. Abstraction is closely related to encapsulation, as it involves defining interfaces to interact with objects and hiding their internal implementation.

In Python, we can use abstract base classes (ABCs) to define abstract classes and abstract methods. ABCs provide a way to enforce the implementation of certain methods in derived classes. The `abc` module in Python provides the necessary tools for working with ABCs.

## Conclusion

This repository serves as a comprehensive guide to Object-Oriented Programming in Python, focusing on classes and methods. By exploring the fundamental concepts of OOP and their implementation in Python, you will gain a solid understanding of how to utilize OOP principles to create modular, reusable, and scalable code.

Feel free to dive into the code examples and experiment with different scenarios to enhance your understanding of OOP in Python.

Happy coding!