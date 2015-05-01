class DNode:
    NextId = 0
    
    def __init__(self):
        self.id = (DNode.NextId)+1
        self.final = False
        self.edges = {}
		
	def setFinal(self):
		self.final = True

class Dawg:

    def __init__(self):
        self.previous = ""
        self.root = DNode()

        # Nodes unchecked for duplication.
        self.uncheckedNodes = []

        # Nodes checked.
        self.reducedNodes = {}

    def insert(self, word):
	
		# Alphabetical order check.
        if word < self.previous:
            raise Exception("Words must be inserted in alphabetical order.")

        # find common prefix between word and previous word
        prefixIndex = 0
        x = min(len(word),len(self.previous))
        for i in range( x ):
            if word[i] != self.previous[i]: break
            prefixIndex += 1

        # Check the uncheckedNodes for redundant nodes, proceeding from last
        # one down to the common prefix size. Then truncate the list at that
        # point.
        self.reducer(prefixIndex)

        # add the suffix, starting from the correct node mid-way through the
        # graph
        if len(self.uncheckedNodes) == 0:
            node = self.root
        else:
            node = self.uncheckedNodes[-1][2]

        for l in word[prefixIndex:]:
            nextNode = DNode()
            node.edges[l] = nextNode
            self.uncheckedNodes.append( (node, l, nextNode) )
            node = nextNode

        node.setFinal()
        self.previous = word # Prepares for next addition via this checker

    def finish( self ):
        self.reducer( 0 );

    def reducer( self, downTo ):
        x = len(self.uncheckedNodes)-1
        for i in range( x, downTo - 1, -1 ):
            (first, l, child) = self.uncheckedNodes[i];
            if child in self.minimizedNodes:
                first.edges[l] = self.minimizedNodes[child]
            else:
                self.minimizedNodes[child] = child;
            self.uncheckedNodes.pop()

    def lookup( self, word ):
        n = self.root
        for l in word:
            if l not in n.edges: return False
            n = n.edges[l]

        return True
