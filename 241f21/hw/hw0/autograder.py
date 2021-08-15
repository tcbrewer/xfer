# Autograder

# This will attempt to perform intended tasks for Sortable, SortableNat, and SortableSet
# For each task, the autograder will:
#  - Define some expected behavior for some use case
#  - Perform the use case
#  - Award "points" if the result is as expected
#  - Either not award points (not too bad) or cause an error (pretty bad) if the result is not as expected

# This is a script to do the tests and print out what's happening
def singleTest(desc, target, val, pts):
	print("AUTOGRADER: " + desc)
	print(" - Expected Value: " + str(target))
	print(" - Observed Value: " + str(val))
	score = 0
	if (val == target):
		score = 5
		pts = pts + 5
	print("POINTS: This section: " + str(score).zfill(2) + "/05 Total: " + str(pts).zfill(3) + "/100\n")	
	return pts

points = 0

print("\n --- AUTOGRADER: SORTABLE ---\n") # This should all be correct from the provided code
from sortable import Sortable
s1 = Sortable()
s2 = Sortable()

print("AUTOGRADER: Sortable Set/Get Testing: 15 pts\n")
points = singleTest("Checking Default Data Value", 0, s1.getData(), points)
s2.setData('word')
points = singleTest("Checking Data Value After Setting Value to Some String (\'word\')", "word", s2.getData(), points)
s2.setData(1)
points = singleTest("Checking Data Value After Setting Value to Integer (1)", 1, s2.getData(), points)

print("AUTOGRADER: Sortable Comparison Testing: 15 pts\n")
points = singleTest("Checking Sortable(1).greaterThan(Sortable(0))", True, s2.greaterThan(s1), points)
points = singleTest("Checking Sortable(0).greaterThan(Sortable(1))", False, s1.greaterThan(s2), points)
s2.setData(0)
points = singleTest("Checking SortableNat(0).greaterThan(SortableNat(0))", False, s1.greaterThan(s2), points)

print("\n --- AUTOGRADER: SORTABLENAT ---\n")
from sortableNat import SortableNat
nat1 = SortableNat()
nat2 = SortableNat()

print("AUTOGRADER: SortableNat Constructor Testing: 05 pts\n")
points = singleTest("Checking SortableNat Default Data Value", 1, nat1.getData(), points)

print("AUTOGRADER: SortableNat Set/Get Testing: 15 pts\n")
nat1.setData("word")
points = singleTest("Checking Data Value After Setting Value to Non-integer (\'word\')", 1, nat1.getData(), points)
nat1.setData(-1)
points = singleTest("Checking Data Value After Setting Value to Integer < 0 (-1)", 1, nat1.getData(), points)
nat2.setData(2)
points = singleTest("Checking Data Value After Setting Value to Some Natural Number (2)", 2, nat2.getData(), points)

print("AUTOGRADER: SortableNat Comparison Testing: 15 pts\n")
points = singleTest("Checking SortableNat(2).greaterThan(SortableNat(1))", True, nat2.greaterThan(nat1), points)
points = singleTest("Checking SortableNat(1).greaterThan(SortableNat(2))", False, nat1.greaterThan(nat2), points)
nat2.setData(1)
points = singleTest("Checking SortableNat(1).greaterThan(SortableNat(1))", False, nat1.greaterThan(nat2), points)


print("\n --- AUTOGRADER: SORTABLENAT ---\n")
from sortableSet import SortableSet
set1 = SortableSet()
set2 = SortableSet()

print("AUTOGRADER: SortableSet Set/Get Testing: 10 pts\n")
set1.setData(0)
points = singleTest("Checking Data Value After Setting Value to Integer (0)", set(), set1.getData(), points)
set2.setData({0,1})
points = singleTest("Checking Data Value After Setting Value to Some Set ({0,1})", {0,1}, set2.getData(), points)

print("AUTOGRADER: SortableSet Comparison Testing: 25 pts\n")
points = singleTest("Checking SortableSet({0,1}).greaterThan(SortableSet(set()))", True, set2.greaterThan(set1), points)
points = singleTest("Checking SortableNat(set()).greaterThan(SortableNat({0,1}))", False, set1.greaterThan(set2), points)
set1.setData({'a'})
set2.setData({'b'})
points = singleTest("Checking SortableNat({\'a\'}).greaterThan(SortableNat({\'b\'}))", False, set1.greaterThan(set2), points)
points = singleTest("Checking SortableNat({\'b\'}).greaterThan(SortableNat({\'a\'}))", True, set2.greaterThan(set1), points)
set2.setData({'a'})
points = singleTest("Checking SortableNat({\'a\'}).greaterThan(SortableNat({\'a\'}))", False, set2.greaterThan(set1), points)