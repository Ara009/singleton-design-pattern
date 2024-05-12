from abc import ABCMeta,abstractstaticmethod
class Iperson(metaclass=ABCMeta):
    @abstractstaticmethod
    def print_data():
        """Implemeting child class"""

class personsingleton(Iperson):
    _instance = None

    @staticmethod
    def get_instance():
        if personsingleton._instance==None:
            personsingleton("Default name",0)
        return personsingleton

    def __init__(self,name,age):
        if personsingleton._instance!=None:
            raise RuntimeError('Singleton cannot be instantiate more than once')
        else:
            self.name = name
            self.age = age
            personsingleton._instance=self

    @staticmethod
    def print_data():
        print(f'name :{personsingleton._instance.name},Age: {personsingleton._instance.age}')


p1 = personsingleton("mike",30)
p2 = personsingleton("Jake",12)
p2.print_data()


