# any class inherited from Type is a metaclass
class Human(type):
    @staticmethod
    def __new__(mcs, *args, **kwargs):
        # create object with Type class __new__ method
        # return value is the class object
        class_ = super().__new__(mcs, *args)
        # append a class property
        class_.freedom = True
        # dynamically add class property from kwargs
        if kwargs:
            for name, value in kwargs.items():
                # class_.name = value this would create a "name" property
                setattr(class_, name, value)
        return class_


# python用指定的Human metaclass里的new方法来制造Student class object
# 希望student类创建时自带类属性country, age, freedom, 其中country, age来自于kwargs
class Student(object, metaclass=Human, age=30, country="China"):
    pass


print(Student.freedom)
print(Student.age)
print(Student.country)

