#Name: James Barbi
#Pledge: I pledge my Honor that I have abided by the Stevens Honor System.


def new_list(x):
    '''
    takes a list x
    
    creates a new list of sums of adjacent terms in the original list
    '''
    if x == []:
        return x
    if len(x) == 1:
        return [1]
    return [x[0] + x[1]] + new_list(x[1:])

def pascal_row(row):
    '''
    takes an integer as input, which represents the row number. Row number 0 indicates the single term row, [1]. The input will always be an integer greater than or equal to 0
    
    returns a list of elements found in a certain row of Pascals Triangle
    '''
    if row == 0:
        return [1]
    if row == 1:
        return [1, 1]
    return [1] + new_list(pascal_row(row-1))


def pascal_triangle(n):
    '''
    takes as input a single integer n
    
    returns a list of lists containing the values of the all the rows up to and including row n
    '''
    if n == 0:
        return [[1]]
    if n == 1:
        return [[1], [1, 1]]
    return pascal_triangle(n-1) + [pascal_row(n)]


def test_pascal_row():
    '''
    test the pascal_row function using assert
    '''
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1, 1]
    assert pascal_row(5) == [1, 5, 10, 10, 5, 1]
    assert pascal_row(2) == [1, 2, 1]

def test_pascal_triangle():
    '''
    test the pascal_triangle function using assert
    '''
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1], [1, 1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    assert pascal_triangle(3) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]