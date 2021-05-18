from region import Region
from product import Product
from operator import Operator
from machine import Machine
import time
class Operation:
    machine: Machine
    operator: Operator
    amount: int
    start_time: time.struct_time
    end_time: time.struct_time

    def __init__(self,m,o,a,s_t,e_t):
        self.machine = m
        self.operator = o
        self.amount = a
        self.start_time = s_t
        self.end_time = e_t
        pass

#initilization

oper = Operation(Machine("Ползуновский вечный двигатель"),Operator("Миханил","Петров","Васильевич"),100,time.gmtime(time.time()),time.gmtime(time.time()+20000))
print(oper.machine.name)