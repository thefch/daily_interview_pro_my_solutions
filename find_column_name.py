#date: 21/06/2020

# Description:
# In many spreadsheet applications, the columns are marked with letters. 
# From the 1st to the 26th column the letters are A to Z. 
# Then starting from the 27th column it uses AA, AB, ..., ZZ, AAA, etc
# Given a number n, find the n-th column name.

ALPHABET_LEN = 26
alphabet = [chr(i) for i in range(65,65+ALPHABET_LEN,1)]
class Node:
    def __init__(self,val):
        self.value = val
        self.children = []
    
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
    
    def add_letter_children(self):        
        for i in alphabet:
            self.children.append(Node(str(self.value)+i))
    
class Tree:
    def __init__(self,val):
        self.root = Node(val)

        self.init()
    
    def __str__(self):
        return str(self.root)
        
    def init(self):
        node = self.root
        for i,x in enumerate(alphabet):
            node.children.append(Node(x))
        
        for i,x in enumerate(alphabet):
            node.children[i].add_letter_children()
            for j,y in enumerate(alphabet):
                node.children[i].children[j].add_letter_children()     
                  
        
    
class Solution:
    def __init__(self):
        pass
    
    def column_name(self,num):
        tree = Tree('')
        node = tree.root
        count =0
        letter = None
        j=0
        
        while True:

            for i,x in enumerate(node.children):
                current_letter = str(x.value)
                if count == num-1:
                    letter = current_letter
                # print(current_letter,end=' ')
                count +=1
                
                
            if j >= 3:
                break
            # # print([j.value for j in node.children])
            # print(j)
            node = node.children[j]
            # print(j)
            
            j+=1
        return letter
        
        
        

print(Solution().column_name(26))#Z
print(Solution().column_name(27))#AA
print(Solution().column_name(28))#AB
print(Solution().column_name(29))#AC
print(Solution().column_name(30))#AD
print(Solution().column_name(ALPHABET_LEN))#Z

print(Solution().column_name(200))#Z


    