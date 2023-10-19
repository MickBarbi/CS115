#Name: James Barbi
#Pledge: I pledge my Honor that I have abided by the Stevens Honor System.

def change(amount, coins):
    """
    inputs a positive integer amount and a list coins containing integers representing different coin values

    returns an integer that represents how many coins from the list it takes to add up to the given amount, with infinity being impossible
    """
    if amount == 0:
        return 0
    if coins == []:
        return float("inf")
    if amount < 0:
        return float("inf")
    if amount in coins:
        return 1
    use_it = 1 + change(amount - coins[-1], coins)
    lose_it = change(amount, coins[:-1])
    return min(use_it, lose_it)