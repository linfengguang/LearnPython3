# -*- coding: utf-8 -*-


class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

    def eat(self):
        print('Eating fish...')

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


if __name__ == '__main__':
    dog = Dog()
    cat = Cat()
    dog.run()
    dog.eat()
    cat.run()
    cat.eat()
    def run_twice(animal):
        animal.run()
        animal.run()

    run_twice(Animal())
    run_twice(Dog())
    run_twice(Tortoise())
    print(type(run_twice))
    print(dir(Animal))

