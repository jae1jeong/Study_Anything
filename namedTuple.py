import collections


Employee =  collections.namedtuple('Person',['name','id'])
employee1 = Employee('David','4011')

print(employee1)
print(type(employee1))

name, id = employee1
print(name,id)

class EmployeeClass:
    def __init__(self,name,id,org):
        self.name  = name
        self.id = id
        self.org = org

employee2 = EmployeeClass('DAVE','4011','SALES')
print(employee2.name,employee2.id,employee2.org)



