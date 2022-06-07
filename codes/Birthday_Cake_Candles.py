
'''You are in charge of the cake for a childs birthday. You have decided the cake 
will have one candle for each year of their total age. They will only be able 
to blow out the tallest of the candles. Count how many candles are tallest.

Example
Sample Input 0

4
3 2 1 3
Sample Output 0

2
Explanation 0

Candle heights are . The tallest candles are  units, and there are  of them.

'''



def birthdayCakeCandles(candles):
    # Write your code here
    
    candles.sort()
    highest_number = candles[-1]
    return(candles.count(highest_number))