class Graph:
    nodes = {}
    def addLine(self,node1,node2,length):
        try:
            self.nodes[node1][node2] = length
            self.nodes[node2][node1] = length
        except:
            raise Exception(f"ADDLINE: Заданная точка не существует.({node1},{node2},{length})")
        pass
    def addNode(self,node):
        try:
            if self.nodes[node]:
                raise Exception(f"ADDNODE: Заданная точка существует.({node})")
        except:

            self.nodes[node] = {}
        pass
    def getNodeRaw(self,node):
        return self.nodes[node]
        pass
    def getNodesRaw(self):
        return self.nodes
        pass
    def getNames(self):
        return list(self.nodes.keys())
        pass
    def getShorter(self,node):
        mini = {}
        while True:
            
            pass


a = Graph()
a.addNode("A")
a.addNode("B")
a.addNode("C")
a.addNode("D")
a.addNode("E")

a.addLine("A","B",7)
a.addLine("A","C",7)
a.addLine("A","D",10)
a.addLine("D","C",1)
a.addLine("D","E",4)
a.addLine("E","C",6)
a.addLine("B","C",5)

print(a.getNames())
