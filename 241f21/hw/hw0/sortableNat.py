# a "Sortable" class contains
# Private (prefixed with two underscores, not visible to users of the object)
# - a __data field, that contains the sortable data
# - a __isAppropriate method, that determines if an argument is appropriate
# Public
# - a getData method that returns the data
# - a setData method that updates the data if the input argument is appropriate, and returns true if successful
# - a constructor __init__ that initializes with a default value
# - a greaterThan method given another sortable s, returns true if data is greater than s.data

# a Nat (natural number) is an integer that is greater than zero.
# (In some cases (though not for this assignment) they may include zero.)
# Some languages support nats directly https://hackage.haskell.org/package/base-.14.1.0/docs/GHC-Natural.html#t:Natural

class SortableNat():
	def __repr__(self):
		return 'Sortable(' + str(self.__data) + ')'
	def __str__(self):
		return 'Sortable(' + str(self.__data) + ')'
	

	def __init__(self):
		self.__data = 1 
		

	def __isAppropriate(self,arg):
		if type(arg) != type(1):
			return False
		if arg < 0 or arg ==0:
			return False
		else:
			return True
		
	def setData(self,arg):
		if self.__isAppropriate(arg)  == True:
			self.__data = arg
			return True
		return False
		
	def getData(self):
		return self.__data
	
	def greaterThan(self, arg):
		return self.__data > arg.getData()

