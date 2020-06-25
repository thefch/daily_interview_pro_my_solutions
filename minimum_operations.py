# date: 04/06/2020

# Description:
# You are only allowed to perform 2 operations,
#  multiply a number by 2, or subtract a number by 1. 
# Given a number x and a number y, 
# find the minimum number of operations needed to go from x to y.

from random import randint

# Node class for the tree
class Node: 
  
  # leafs are named as multiply and substract instead of left and right
  def __init__(self,val): 
      self.value = val  
      self.multiply = None
      self.substract = None
  
  # for debugging
  def __str__(self):
    print(self.value,' | ',self.multiply.value,'  ',self.substract.value)
    
  # add operation to the node with the current value
  def add(self,operation,total):
    if operation == 'm':
      self.multiply = Node(total)
    elif operation == 's':
      self.substract = Node(total)
      
# Tree class of Breadth-First-Search
class BFS:
  def __init__(self,val):
    self.root = Node(val)
  
  # checks if the current operation already exists in the tree
  def exists(self,operations):
    node = self.root
    for i in operations:
      if i == 'm':
        node = node.multiply
      elif i == 's':
        node = node.substract
      
      if node == None:
        return False

    if node.value == None:
      return False
    return True
    

class Solution:
  def __init__(self):
    self.total = 0
    self.bfs = BFS(0)
    
  
  def mul(self):
    self.total=self.total*2
    
  def sub(self):
    self.total=self.total-1
    
  # returns a random operation, multiplication or substraction
  def get_operation(self):
    option = randint(1,2)
    if option==1:
      return 'm'
    if option==2:
      return 's'  
  
  def min_operations(self,x, y):
    self.total = x
    node = self.bfs.root
    operations = []
    count = 0
    found = False
    finish = False
    final = []
    count_totals = 0
    
    while not finish:
      
      # input() for debugging
      op = self.get_operation()
      operations.append(op)
      if not self.bfs.exists(operations):
        if op == 'm':
          
          node.add(op,self.total)
          self.mul()
          node = node.multiply
        elif op == 's':
          node.add(op,self.total)    
          self.sub()
          node = node.substract
        
        
      print(op,' ',self.total, '  ->',self.bfs.exists(operations))
      if self.total == y:
        count_totals += 1
        print('Found Y =>',self.total)
        
        # skip the first element, it the initial number x
        final.append(operations[1:])
        operations = []
        self.total = x

      #  RESET CURRENT STATUS
      # for cases when the goal value is positive
      if y>0 and (self.total > y or self.total < 0):
        print('Reset current parent node')
        node = self.bfs.root
        self.total = x
        operations = []
      
      # for cases when the goal value is negative
      if y<0 and (self.total < y or self.total > 0):
        print('Reset current parent node')
        node = self.bfs.root
        self.total = x
        operations = []
      
      if found and count > y+50:
        finish = True
      elif count_totals > 1 and count > y+50:
        finish = True
        
      count += 1
      
    # look up for the minimum operations
    less = final[0]
    for i in final:
      if len(i) < len(less) :
        less = i
    return len(less)
        
    
    
# s - substract
# m - multiply
print(Solution().min_operations(6, 20))
# example: 6
# => (((6 - 1) * 2) * 2) = 20 : 3 operations needed only
# print 3
