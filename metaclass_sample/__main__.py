class Prop:
    def __init__(self, attr):
        self._attr = f'_{attr}'

    def get(self, obj):
        if not hasattr(obj, self._attr):
            return None
        print(obj)
        return getattr(obj, self._attr)

    def set(self, obj, value):
        print(obj)
        return setattr(obj, self._attr, value)


class Human(type):
    @staticmethod
    def __new__(mcs, *args, **kwargs):
        cls_ = super().__new__(mcs, *args)
        print(type(cls_))
        for prop_name in cls_.props:
            prop = Prop(prop_name)
            p_object = property(fget=prop.get, fset=prop.set)
            setattr(cls_, prop_name, p_object)

        return cls_

# add props dynamically to object
class Student(object, metaclass=Human):
    # class level property
    props = ["name", "age"]


def human(cls):
    return Human(cls.__name__, cls.__bases__, dict(cls.__dict__))


@human
class Man:
    props = ["name", "age"]

student = Student()
print(student.name)
student.name = "Jack"
print(student.name)
student.age = 15
student.name = "Rose"
print(student.name)

man = Man()
print(man.name)
man.name = "Tom"
print(man.name)



