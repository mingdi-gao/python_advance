class Student:
    def greeting(self):
        print("Hello student")


print(type(Student))
print(isinstance(Student, type))



class_body = """
def greeting(self):
    print("Hello customer")
"""
class_dict = {}
# transform class body into a dict
exec(class_body, globals(), class_dict)

# create class named "Customer", dynamically
Customer = type("Customer", (object,), class_dict)

c = Customer()
c.greeting()
