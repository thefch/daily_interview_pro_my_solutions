# date: 27/06/2020

# Description:
# Implement auto-completion.
# Given a large set of words (for instance 1,000,000 words)
# and then a single word prefix, find all words that it can complete to.

class Node:
    def __init__(self,val):
        self.value = val
        self.children = []
        
    # return the node that hold the specified letter
    def get(self,letter):
        for i in self.children:
            if letter == i.value:
                return i
        
        return None
    
    # combine all the concecutives children to produce a string
    def get_word(self,out):
        out = str(self.value)
        for i in self.children:
            if i.children is not None:
                out += i.get_word(out)
            else:
                out += i.value
        return out
        
    # add a letter to a current node
    def add(self,letter):
        self.children.append(Node(letter))

    def __str__(self):
        out =''
        if self.children != None:
            out += ' '*(len(self.children))
            out += str(self.value) 
        else:
            out += str(self.value)
        out +='\n| '
        for j,i in enumerate(self.children):
            out += i.value + ' '+str(j)+' | '
        return out        
    
class Tree:
    def __init__(self, val):
        self.root = Node(val)
        
    def __str__(self):
        return str(self.root)
    
    # add a word to the tree
    def add_word(self, word):
        node = self.root
        w = list(word)
           
        for i in w:
            temp = node.get(i)
            if temp is None:
                node.add(i)
                node = node.get(i)       
            else:
                node = temp
    
    # returns the children of a specifiec string node 
    def get_children(self,word):
        node = self.root
        w = list(word)
        for i in w:
            node = node.get(i)
        
        return len(node.children),node.children      
    
class Solution:
    def __init__(self):
        self.tree = Tree('')
        
    def build(self,words):
        print('Building tree with words....')
        for w in words:
            self.tree.add_word(w)
      
      
    def autocomplete(self, word):
        print('Autocomplete started... : `',word,'`')
        
        _,lst = self.tree.get_children(word)

        for i in range(len(lst)):
           
            x = lst[i].get_word('')
            lst[i]= word+x
        return lst


s = Solution()
s.build(['dog', 'dark', 'cat', 'door', 'dodge'])
print(s.autocomplete('do'))
# ['dog', 'door', 'dodge']
