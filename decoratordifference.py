class MyClass:
    class_variable =0

    def __init__(self,instance_variable):
        self.instance_variable = instance_variable

    @staticmethod
    def static_method(x,y):
        return x+y

    @classmethod
    def class_method(cls,x):
        cls.class_variable +=x
        return cls.class_variable

result_static =MyClass.static_method(5,3)
print(f"static method: {result_static}")

result_class = MyClass.class_method(7)
print(f"class method result:{ result_class}" )

instance = MyClass(20)
result_class_instance= instance.class_method(7)
print(f"class method result (from instance:{result_class_instance})")

result_class=MyClass.class_method(7)
print(f"result_class is {result_class}")