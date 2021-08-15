# a "Sortable" class contains
# Private (prefixed with two underscores, not visible to users of the object)
# - a __data field, that contains the sortable data
# - a __isAppropriate method, that determines if an argument is appropriate
# Public
# - a getData method that returns the data
# - a setData method that updates the data if the input argument is appropriate, and returns true if successful
# - a constructor __init__ that initializes with a default value
# - a greaterThan method given another sortable s, returns true if data is greater than s.data

# a Set is a collection of values.  https://docs.python.org/2/library/stdtypes.html#set
# The values are not ordered within sets, and
# there is no built-in sorting method for sets.
# Sort them by size, and break ties by comparing them alphabetically when converted to strings using str()
# So {1,2,3,4} > {1,2,3} (4 comes AFTER 3, so 4 is greater)
# And {"b"} > {"a"} (b comes AFTER a, so b is greater)
class SortableSet(Sortable):
	   
	# TODO: Your code here