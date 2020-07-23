from numpyGet import get_digits
from norvig_soln import solve
from norvig_soln import display
from norvig_soln import parse_grid


def soln(path):
	grid = get_digits(path)
	solved = solve(grid)
	solved_grid = ''.join(solved.values())
	return grid, solved_grid


'''
print(grid)


#print(len(grid))


print('\n')
print('\n')
print('\n')
print('\n')
#print(solved)
print('\n')
print('\n')
print('\n')
print(solved_grid)
print('\n')
print('\n')
print('\n')
#print(display(solved))
'''