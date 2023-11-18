// You are given an integer array height of length n. There are n vertical
// lines drawn such that the two endpoints of the ith line are (i, 0) and
// (i, height[i]).

// Find two lines that together with the x-axis form a container, such that
// the container contains the most water.

// Return the maximum amount of water a container can store.

// Notice that you may not slant the container.

// Example 1:
// Input: height = [1,8,6,2,5,4,8,3,7]
// Output: 49
// Explanation: The above vertical lines are represented by array
// [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
// container can contain is 49.

// Example 2:
// Input: height = [1,1]
// Output: 1
#include <stdio.h>
#include <stdbool.h>
int findArea(int *height, int leftptr, int rightptr){
    return (height[leftptr] > height[rightptr]) ?
    (height[rightptr] * (rightptr - leftptr)) :
    (height[leftptr] * (rightptr - leftptr));
}

int maxArea(int* height, int heightSize){
    int leftptr = 0;
    int rightptr = heightSize - 1;
    int maxArea = -1;

    while(leftptr < rightptr){
        int curArea = findArea(height, leftptr, rightptr);
        if(curArea > maxArea) maxArea = curArea;
        // Only real difficult part is moving the pointers towards each other.
        // If you can figure this out, then you are golden. You are trying to
        // maximize both heights at any given iteration, since the smaller
        // of the two heights is the determining factor in how much you can
        // store.
        if(height[leftptr] > height[rightptr]) rightptr--;
        else leftptr++;
    }

    return maxArea;
}
