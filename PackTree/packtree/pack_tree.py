# !/usr/bin/env python
# coding: utf-8

class Tree:
  def __init__(self, V, U):
    self.root = V[0]
    self.node = V
    self.edge = U
    self.leafs = [item for item in [x[1] for x in U] if item not in [x[0] for x in U]]

  def get_root(self):
    return self.root

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
      
  def subtree(self, subroot):
    subT = [subroot]

    current_child = self.childs(subroot)

    if current_child != []:
      for i in range(len(current_child)):
        subT.append(self.subtree(current_child[i]))

    return subT
  
  def add_metV(self):
    S = list(self.nodes())
    
    metV = {node: 1 for node in self.node}

    while S:
        current_node = S.pop()
        metV[current_node] = 1 if self.isleaf(current_node) else sum([metV[i] for i in self.childs(current_node)])
        S.extend(self.childs(current_node)[::-1])

    return metV
  
  def add_widthV(self):
    S = list(self.nodes())
    
    widthV = {node: 0 for node in self.node}

    while S:
      current_node = S.pop()
      if self.childs(current_node) != []:
        T = [widthV[node] for node in self.childs(current_node)]
        T = sorted(T, reverse=True)
        T = [T[i]+i for i in range(len(self.childs(current_node)))]
        T.append(len(self.childs(current_node)))
        widthV[current_node] =  max(T)
      S.extend(self.childs(current_node)[::-1])
      
    return widthV
  
  def add_numP(self, met):
    numP = {}

    S = [(self.root, met[self.root])]

    num = len(self.node)
    # вычисление номеров вершин в укладке
    while S:
      cur_node = S.pop()[0]

      numP[cur_node] = num
      num -= 1
      if met[cur_node] != 1:
        ch = self.childs(cur_node)
        ch = sorted(ch, key=lambda m: met[m], reverse=True)
        S += [(x, met[x]) for x in ch]

    return numP

  def Pack_min_length(self):
    # вычисление меток для вершин
    met = self.add_metV()
    # print(met)
    return self.add_numP(met)
  
  def Pack_min_width(self):
    width = self.add_widthV()
    # print(width)
    return self.add_numP(width)


# In[]:  дерево для теста

Example1 = Tree(["root", "x0", "x1", "x2", "y0", "y1", "z0", "z1", "z2", "u0", "u1", "v0", "v1", "w0", "w1"], [("root", "x0"), ("root", "x1"), ("root", "x2"),
                        ("x1", "y0"), ("x1", "y1"),
                          ("x0", "z0"), ("x0", "z1"), ("x0", "z2"),
                          ("y0", "u0"), ("y0", "u1"), 
                          ("z0", "v1"), ("z0", "v0"),
                          ("v0", "w0"), ("v0", "w1")])

Example2 = Tree(["root", "x0", "x1", "z0", "z1", "z2", "w0", "y1", "y0", "u0", "u1"], [("root", "x0"), ("root", "x1"),
                                                                                       ("x1", "w0"),
                                                                                       ("x0", "z0"), ("x0", "z1"), ("x0", "z2"),
                                                                                       ("w0", "y1"), ("w0", "y0"),
                                                                                       ("y0", "u0"), ("y0", "u1")])
# In[]: вывод дерева

def main(): 
  print(Example2.Pack_min_width())

if __name__ == "__main__":
  main()