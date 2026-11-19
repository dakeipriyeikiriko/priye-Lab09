# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    for i in range (len(nums)):
        for j in range (i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    
two_sum([2, 7, 11, 15], 9)
    # Outline (write your plan here first):
    # create a function two_sum(nums, target)
    # make a for loop that checks through every item in the list
    # make another for loop that checks evry item in the list apart from the first item
    # sum them and if they equal the target return the idexes of those numbers
    #   ...
    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.
    


def max_profit(prices):
     
    # Outline:
    # set the minimum price to the first item in the list prices[0]
    # set the max profit to 0
    # make a for loop that goes through every item in the list 
    # make an if statement to check if price is lower than minimum price and if it is set that to the new min price
    # make a function that calculates profit
    # make an if statement to check if profit is greater than max profit and if it is make that profit the new max profit 
    # return max_profit
    #   ...
    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.
    if (len(prices)) == 0:
     return 0
    
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        
        profit = price - min_price
        
        if profit > max_profit:
            max_profit = profit
    return max_profit
                
   



def max_subarray(nums):
    # Outline:
    #   ...
    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.
    
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        if current_sum + nums[i] < nums[i]:
            current_sum = nums[i]
        else:
            current_sum = current_sum + nums[i]

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass


if __name__ == "__main__":
    main()
