# Problem 1: Square Root of an integer

## Approach: Binary Search

we should find floored square root. it is a value between integers.
For example, √5 is between √4 and √9.

√4 < √5 < √9 -> 2 < √5 < 3

So we just need to find the value of 2.

The square root is always less than the square of the number
and greater than or equal to 0. So we can find it with a binary search.


## Complexity Analysis

- Time complexity: `O(log(n))`.

    Because it always cuts half.

- Space complexity: `O(log(n))`.

    it takes up space in memory to the call stack.