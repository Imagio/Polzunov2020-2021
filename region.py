from machine import Machine
class Region:
    name: str
    list_of_machines: [Machine]
    def __init__(self,name,list_of_machines):
        self.name = name
        self.list_of_machines = list_of_machines
        pass