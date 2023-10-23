import networkx as nx
import matplotlib.pyplot as plt

class Tree:
  def __init__(self, V, U):
    self.node = V
    self.edge = U
    self.leafs = [item for item in [x[1] for x in U] if item not in [x[0] for x in U]]
  
  def root(self):
    return self.node[0]

  def nodes(self):
    return self.node
  
  def edge(self):
    return self.edge
  
  def leaf(self):
    return self.leafs
  
  def isleaf(self, node):
    return node in self.leafs
  
  def childs(self, parent):
    return [item[1] for item in self.edge if item[0] == parent]
  
  def parent(self, child):
    for item in self.edge:
      if item[1] == child:
        return item[0]
  
  def add_metV(self, start_node):
    S = self.node
    
    metV = {node: 1 for node in self.node}

    while S:
        current_node = S.pop()
        metV[current_node] = 1 if self.isleaf(current_node) else sum([metV[i] for i in self.childs(current_node)])
        S.extend(self.childs(current_node)[::-1])

    return metV
  
  def Pack_min_length(self):
    pass
  

# In[]:  дерево для теста

Example = Tree(["root", "x0", "x1", "x2", "y0", "y1", "z0", "z1", "z2", "u0", "u1", "v0", "v1", "w0", "w1"], [("root", "x0"), ("root", "x1"), ("root", "x2"),
                        ("x1", "y0"), ("x1", "y1"),
                          ("x0", "z0"), ("x0", "z1"), ("x0", "z2"),
                          ("y0", "u0"), ("y0", "u1"), 
                          ("z0", "v1"), ("z0", "v0"),
                          ("v0", "w0"), ("v0", "w1")])

# In[]: вывод дерева

print(Example.add_metV("w1"))

# nx.draw(Example, with_labels=True, font_weight='bold')
# plt.show()