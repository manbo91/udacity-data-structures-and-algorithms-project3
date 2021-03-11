# Problem 3: Rearrange Array Elements

## Approach: Heap Sort

We want to maximize the sum of two numbers, we just pull the
maximum number once to make two numbers.

So I used max-heap.

## Complexity Analysis

- Time complexity: `O(n log(n))`. 

    The time complexity of heap sort is O(n log(n)).
    Creating two numbers is the process of creating a string,
    which is O(n).

- Space complexity: `O(n)`. 

    The space compleixty is O(n) by taking n to make two numbers.