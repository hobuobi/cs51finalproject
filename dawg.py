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
        self.minimizedNodes = {}

    def insert(self,word):
	
		# Alphabetical order check.
        if word < self.previous:
            raise Exception("Words must be inserted in alphabetical " +
                "order.")

        # find common prefix between word and previous word
        prefixIndex = 0
        for i in range( min( len( word ), len( self.previousWord ) ) ):
            if word[i] != self.previousWord[i]: break
            prefixIndex += 1

        # Check the uncheckedNodes for redundant nodes, proceeding from last
        # one down to the common prefix size. Then truncate the list at that
        # point.
        self._minimize(prefixIndex)

        # add the suffix, starting from the correct node mid-way through the
        # graph
        if len(self.uncheckedNodes) == 0:
            node = self.root
        else:
            node = self.uncheckedNodes[-1][2]

        for l in word[prefixIndex:]:
            nextNode = DNode()
            node.edges[l] = nextNode
            self.uncheckedNodes.append( (node, letter, nextNode) )
            node = nextNode

        node.setFinal
        self.previous = word # Prepares for next addition via this checker

    def finish( self ):
        self._minimize( 0 );

    def _minimize( self, downTo ):
        # proceed from the leaf up to a certain point
        for i in range( len(self.uncheckedNodes) - 1, downTo - 1, -1 ):
            (parent, letter, child) = self.uncheckedNodes[i];
            if child in self.minimizedNodes:
                # replace the child with the previously encountered one
                parent.edges[letter] = self.minimizedNodes[child]
            else:
                # add the state to the minimized nodes.
                self.minimizedNodes[child] = child;
            self.uncheckedNodes.pop()

    def lookup( self, word ):
        node = self.root
        for letter in word:
            if letter not in node.edges: return False
            node = node.edges[letter]

        return True
