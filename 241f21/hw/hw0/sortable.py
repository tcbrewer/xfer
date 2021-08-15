# a "Sortable" class contains
# Private (prefixed with two underscores, not visible to users of the object)
# - a __data field, that contains the sortable data
# - a __isAppropriate method, that determines if an argument is appropriate
# Public
# - a getData method that returns the data
# - a setData method that updates the data if the input argument is appropriate, and returns true if successful
# - a constructor __init__ that initializes with a default value
# - a greaterThan method given another sortable s, returns true if data is greater than s.data

class Sortable:

	# niceties for printing	
	def __repr__(self):
		return 'Sortable(' + str(self.__data) + ')'
	def __str__(self):
		return 'Sortable(' + str(self.__data) + ')'
	
	# constructor
	def __init__(self):
		self.__data = 0 # default value
		
	# private isAppropriate method - since this isn't any particular sortable, allow any data at all
	def __isAppropriate(self,arg):
		return True
		
	# setting data if appropriate
	def setData(self,arg):
		if self.__isAppropriate(arg):
			self.__data = arg
			return True
		return False
		
	def getData(self):
		return self.__data
	
	def greaterThan(self, arg):
		return self.__data > arg.getData()