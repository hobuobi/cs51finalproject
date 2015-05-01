class Branch: 
	
	def __init__(self):
		self.node = DNode()
		self.t_node = DNode()
		self.chr = ''
	def __init__(self, c):
		self.o_node = DNode()
		self.t_node = DNode()
		self.chr = c
	def __init__(self,c,f,t):
		self.o_node = f
		self.t_node = t
		self.chr = c
	def getNode(): 
		return self.node 
	
		
class DNode:
	
	def __init__(self):
		self.branches_to = []
		self.branches_from = []
		self.final = False
		
	def __init__(self,bt,bf):
		self.branches_to = []
		self.branches_from = []
		self.final = True
		
	def setFinal():
		self.final = True
		
	def insert (self,word):
		# Phase 1 - create basic trie
		index = 0
		currentNode = self
		while (index<len(word)):
			exist = false
			for b in currentNode.branches_to:
				if b.chr == word[index]:
					currentNode = b.node
					exist = true
					index+= 1
					break
					
			if (not exist):
				newNode = DNode()
				newBranch = Branch(b.chr,currentNode,newNode)
				(newNode.branches_from).append(newBranch)
				currentNode = newNode
		# Phase 2 - collapse
		
	def search (word):
		currentNode = self
		while (index<len(word)):
			exist = false
			nextChar = ''
			for b in currentNode.branches_to:
				if b.chr == word[index]:
					nextChar = b.chr
					currentNode = b.node
					exist = true
					index+= 1
					break
			if(index == len(word)):
				print('')
			elif(not exist):
				print('Not found.')
			else:
				print(search+nextChar)			
