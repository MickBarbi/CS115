#Name: James Barbi
#Pledge: I pledge my Honor that I have abided by the Stevens Honor System.

def knapsack(capacity, itemList):
    '''
    takes in an integer 'capacity' and a list of list 'itemList' formatted [int, int] with the first int being a weight and the second being a value

    returns the greatest value of collected items and the list of items to get there, while not allowing weight to exceed capacity
    '''
    if capacity == 0:
        return [0, []]
    if capacity <= 0:
        return [0 - float("inf"), []]
    if itemList == []:
        return [0, []]
    used = knapsack(capacity - itemList[0][0], itemList[1:])
    use_it = [itemList[0][1] + used[0], [itemList[0]] + used[1]]
    lose_it = knapsack(capacity, itemList[1:])
    if use_it[0] > lose_it[0]:
        return use_it
    else:
        return lose_it