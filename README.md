# CSCA08_A2 Elevation Map Analysis

In this assignment, we are interested in analysing the elevation of a section of the Earth's surface. We will represent the section of Earth as a square matrix of numerical values. A square matrix has equal dimensions: the number of rows is the same as the number of columns. Each value in the matrix corresponds to the elevation of the Earth at that particular location. For example, an area the size of 1 square kilometre of Earth could be encoded as a 1000x1000 matrix. Each cell of the matrix contains the elevation of a single square meter. Here, the value at cell [500, 500] of the matrix, would be the elevation at approximately the middle of the original 1 square kilometre section.

For this assignment, you will implement several functions which will allow someone with such a matrix of values to perform meaningful analysis of the Earth elevation data.

**Assignment Terminology**

**elevation map**: We will represent an elevation map in Python as a List[List[int]]. 
* An elevation map's outer list and inner lists will be non-empty.
* An elevation map will be square. That is, the outer list List[List[int]] has the same length as each inner list List[List[int]], and the number of inner lists is equal to the length of the outer list. For example, in the figure above, the 3x3 elevation map is represented with a nested list of length 3, which contains 3 sub-lists, each of length 3.
* An elevation map will only contain positive integers.
  
**cell**: We will represent a cell in Python as a list of 2 non-negative integers (List[int]). Given an elevation map m, we say "cell [i, j]" as a shorthand for m[i][j].

**adjacent cell**: We will say that cell [i, j] is adjacent to cell [k, l] if and only if [k, l] equals one of:
[i-1, j-1], [i-1, j], [i-1, j+1], [i, j-1], [i, j+1], [i+1, j-1], [i+1, j], or [i+1, j+1].
 
**sink**: Given an elevation map m, the cell [i, j] is a sink if m[i][j] <= m[k][l] for all adjacent cells [k, l]. With the physical interpretation of an elevation map in mind, water would collect in sinks, since there is no less elevated area in the immediate vicinity for the water to flow to. 

