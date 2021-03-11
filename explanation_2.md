# Problem 2: Search in a Rotated Sorted Array

## Approach: Binary Search

In a special sorted array, we can find to value by dividing a half,
depending on conditions.

Consider the case where the first array we are looking for is not
rotated and rotated.

Next, we can choose half correctly by dividing by if the median is
on the pivot, and if the median is less than the starting point,
and if the median is greater than the string point.

## Complexity Analysis

- Time complexity: `O(log(n))`. 

    Because it always cuts half.

- Space complexity: `O(log(n))`.

    it takes up space in memory to the call stack.