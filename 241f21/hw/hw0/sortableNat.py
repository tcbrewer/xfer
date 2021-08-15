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
# Some languages support nats directly https://hackage.haskell.org/package/base-4.14.1.0/docs/GHC-Natural.html#t:Natural
class SortableNat(Sortable):
	   
	# TODO: Your code here.