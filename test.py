class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._klass = 0
        
class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self._klass = 1
        
    @property
    def klass(self):
        return self._klass
    
    @klass.setter
    def klass(self, klass):
        if klass < 0 or klass > 12:
            raise ValueError('Error class')
        self._klass = klass
        
student = Student('Dat', 22)
student.klass = 112
print(vars(student))