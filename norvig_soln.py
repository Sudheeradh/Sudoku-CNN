def cross(A, B):
    #Cross product oof elements in A and elements in B
    return [a+b for a in A for b in B]

digits = '123456789'
rows = 'ABCDEFGHI'

cols = digits
squares = cross(rows, cols)

unitlist = ([cross(rows, c) for c in cols] + 
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])

units = dict((s, [u for u in unitlist if s in u])
                for s in squares)

peers = dict((s, set(sum(units[s], [])) -set([s])) for s in squares)

# Testing whether units and peers are correct
def test():
    assert len(squares) == 81
    assert len(unitlist) == 27
    assert all(len(units[s]) == 3 for s in squares)
    assert all(len(peers[s]) == 20 for s in squares)
    assert units['A1'] == [['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9'],
                           ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1'],
                           ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']]
    assert peers['A1'] == set(['A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9',
                               'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 
                               'B2', 'B3', 'C2', 'C3'])
    print('All tests pass.')

def test():
    "A set of unit tests."
    assert len(squares) == 81
    assert len(unitlist) == 27
    assert all(len(units[s]) == 3 for s in squares)
    assert all(len(peers[s]) == 20 for s in squares)
    assert units['C2'] == [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'],
                           ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'],
                           ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']]
    assert peers['C2'] == set(['A2', 'B2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2',
                               'C1', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
                               'A1', 'A3', 'B1', 'B3'])
    print('All tests pass.')

# Values will be a dict with squares as keys
# Value of each key will be possible digit for that square 
# Value --> single digit for correct position and multiple digits for uncertain position

def parse_grid(grid):
    # Convert grid (string) into dict
    # {square: digits}
    # return false if a contradiction is detected

    # At start, every square can be any digit; then assign values from grid.

    values = dict((s, digits) for s in squares)
    for s,d in list(grid_values(grid).items()):
        if d in digits and not assign(values, s, d):
            return False
    return values


def grid_values(grid):
    # {square: char} with '0' or '.' for empties
    chars = [c for c in grid if c in digits or c in '0.']
    assert len(chars) == 81
    return dict(list(zip(squares, chars)))

def assign(values, s, d):
    # Eliminates values other than d from values[s] and propagate
    other_values = values[s].replace(d, '')
    if all (eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False

def eliminate(values, s, d):
    #Eliminate d from values[s]; propagate when values or places <= 2
    if d not in values[s]:
        return values # Already eliminated
    
    values[s] = values[s].replace(d, '')
    # --> If square s is reduced to one value d2, eliminate d2 from peers
    if len(values[s]) == 0:
        return False
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False


    # --> If a unit u is reduced to only one place for a value d, then put it there
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False
        elif len(dplaces) == 1:
            # d can only be in one place in unit; assign ther
            if not assign(values, dplaces[0], d):
                return False

    return values


def display(values):
    #Display the values in 2D grid
    width = 1 + max(len(values[s]) for s in squares)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print (''.join(values[r+c].center(width)+('|' if c in '36' else '') for c in cols))
        if r in 'CF': print (line)
        print

def solve(grid): return search(parse_grid(grid))


#Using recursion to search for values


def search(values):
    #Using depth first search and propagation
    if values is False:
        return False #Failed earlier
    if all(len(values[s]) == 1 for s in squares):
        return values # Base case
    
    # Choosing unfilled squares with fewest possibilities
    n,s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d)) for d in values[s])

def some(seq):
    #Return an element of seq thats True
    for e in seq:
        if e: return e
    return False

'''
grid2 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
'''
#grid1 = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
#grid1 = '000230000037000920090007030004070008600402001700010800070800010018000870000051000'
#test()
#print(solve(grid1))



'''
f = '12345'
cu = [c for c in f]
print(cu)
'''
#print(peers)
#print(units)
#print(squares)