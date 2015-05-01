class Branch: 
	
	def __init__(self):
		self.o_node = DNode()
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
	def getONode(self): 
		return self.o_node 
	
	def getTNode(self):
		return self.t_node
	
	def setTNode(self,t):
		self.t_node = t
	
	def setONode(self,f):
		self.o_node = f
class DNode:
	
	def __init__(self):
		self.branches_to = []
		self.branches_from = []
		self.final = False
		
	def __init__(self,bt,bf):
		self.branches_to = []
		self.branches_from = []
		self.final = False
		
	def setFinal(self,x):
		self.final = x
	
	def childCheck(self,xNode, yNode):
		if (len(xNode.branches_to) != len(yNode.branches_to)):
			return False
		else:
			j = 0
			while j < len(xNode.branches_to):
				if (xNode.branches_to)[j] == (yNode.branches_to)[j]:
					childCheck((xNode.branches_to)[j].getTNode(),(yNode.branches_to)[j].getTNode())
				else:
					return False
				j+=1
		return True
				
	def insert (self,word):
		terminalNodes = []
		# Phase 1 - create basic trie
		index = 0
		currentNode = self
		while (index<len(word)):
			print('phase1')
			exist = False
			##bran = Branch('',DNode([],[]),DNode([],[])) 
			for b in currentNode.branches_to:
				print('branches_to')
				if b.chr == word[index]:
					currentNode = b.t_node
					exist = True
					index+= 1
					break
				
			if (not exist):
				newNode = DNode([],[])
				newBranch = Branch(word[index],currentNode,newNode)
				(newNode.branches_from).append(newBranch)
				(currentNode.branches_to).append(newBranch)
				currentNode = newNode
			if(index == len(word)-1):
				terminalNodes.append(currentNode)
				currentNode.setFinal(True)
			index+=1
		# Phase 2 - collapse
		
		for x in terminalNodes:
			if(self.childCheck(currentNode,x)): 
				print('phase2')
				if(currentNode.branches_from != []) and (x.branches_from != []) :
					(currentNode.branches_from)[0].t_node = x

							
	def search (self,word):
		index = 0
		currentNode = self
		while (index<len(word)):
			print('poo1')
			exist = False
			nextChar = ''
			for b in currentNode.branches_to:
				print('b')
				if b.chr == word[index]:
					nextChar = b.chr
					currentNode = b.t_node
					exist = True
					break
					
			index+= 1
		if(index == len(word)):
			print('.')
		if(not exist):
			print('Not found.')
		else:
			print((self.search)+nextChar)			
