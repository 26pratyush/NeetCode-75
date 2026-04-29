#You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
#You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
#Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

#Example 1: Input: prices = [10,1,5,6,7,1]
#Output: 6: Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

#Sliding Window: O(n)
left = 0          
max_profit = 0

for right in range(1, len(prices)):
    if prices[right] > prices[left]:
        profit = prices[right] - prices[left]
        max_profit = max(max_profit, profit)
    else:
        left = right
return max_profit
