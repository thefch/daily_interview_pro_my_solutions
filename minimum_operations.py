# date: 04/06/2020

# Description:
# You are only allowed to perform 2 operations,
#  multiply a number by 2, or subtract a number by 1. 
# Given a number x and a number y, 
# find the minimum number of operations needed to go from x to y.

from random import randint

class Node: 
  def __init__(self,val): 
      self.value = val  
      self.multiply = None
      self.substract = None
  
  def __str__(self):
    print(self.value,' | ',self.multiply.value,'  ',self.substract.value)
    
  def add(self,operation,total):
    if operation == 'm':
      self.multiply = Node(total)
    elif operation == 's':
      self.substract = Node(total)
      
      
class BFS:
  def __init__(self,val):
    self.root = Node(val)
  
  
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
        final.append(operations[1:])
        operations = []
        self.total = x
      
      #  add a compare statement
      # to check more than one way to implement it
      
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
      # if count >2 :
      #   break
      
      if found and count > y+50:
        finish = True
      elif count_totals > 1 and count > y+50:
        finish = True
        
      count += 1
      
    less = final[0]
    for i in final:
      if len(i) < len(less) :
        less = i
    return len(less)
        
    
    
# s - substract
# m - multiply
print(Solution().min_operations(6, 20))
# (((6 - 1) * 2) * 2) = 20 : 3 operations needed only
# print 3
