"""Assignment 2 functions."""

from typing import List


THREE_BY_THREE = [[1, 2, 1],
                  [4, 6, 5],
                  [7, 8, 9]]

FOUR_BY_FOUR = [[1, 2, 6, 5],
                [4, 5, 3, 2],
                [7, 9, 8, 1],
                [1, 2, 1, 4]]

UNIQUE_3X3 = [[1, 2, 3],
              [9, 8, 7],
              [4, 5, 6]]

UNIQUE_4X4 = [[10, 2, 3, 30],
              [9, 8, 7, 11],
              [4, 5, 6, 12],
              [13, 14, 15, 16]]


def compare_elevations_within_row(elevation_map: List[List[int]], map_row: int,
                                  level: int) -> List[int]:
    """Return a new list containing the three counts: the number of
    elevations from row number map_row of elevation map elevation_map
    that are less than, equal to, and greater than elevation level.

    Precondition: elevation_map is a valid elevation map.
                  0 <= map_row < len(elevation_map).

    >>> compare_elevations_within_row(THREE_BY_THREE, 1, 5)
    [1, 1, 1]
    >>> compare_elevations_within_row(FOUR_BY_FOUR, 1, 2)
    [0, 1, 3]

    """
    
    less_than = 0
    equal_to = 0
    greater_than = 0
    
    for nums in elevation_map[map_row]:
        if nums > level:
            greater_than = greater_than + 1
        
        elif nums == level:
            equal_to = equal_to + 1
        
        else:
            less_than = less_than + 1
    
    return [less_than, equal_to, greater_than]


def update_elevation(elevation_map: List[List[int]], start: List[int],
                     stop: List[int], delta: int) -> None:
    """Modify elevation map elevation_map so that the elevation of each
    cell between cells start and stop, inclusive, changes by amount
    delta.

    Precondition: elevation_map is a valid elevation map.
                  start and stop are valid cells in elevation_map.
                  start and stop are in the same row or column or both.
                  If start and stop are in the same row,
                      start's column <=  stop's column.
                  If start and stop are in the same column,
                      start's row <=  stop's row.
                  elevation_map[i, j] + delta >= 1
                      for each cell [i, j] that will change.

    >>> THREE_BY_THREE_COPY = [[1, 2, 1],
    ...                        [4, 6, 5],
    ...                        [7, 8, 9]]
    >>> update_elevation(THREE_BY_THREE_COPY, [1, 0], [1, 1], -2)
    >>> THREE_BY_THREE_COPY
    [[1, 2, 1], [2, 4, 5], [7, 8, 9]]
    >>> FOUR_BY_FOUR_COPY = [[1, 2, 6, 5],
    ...                      [4, 5, 3, 2],
    ...                      [7, 9, 8, 1],
    ...                      [1, 2, 1, 4]]
    >>> update_elevation(FOUR_BY_FOUR_COPY, [1, 2], [3, 2], 1)
    >>> FOUR_BY_FOUR_COPY
    [[1, 2, 6, 5], [4, 5, 4, 2], [7, 9, 9, 1], [1, 2, 2, 4]]

    """
    
    a = start[0]
    b = start[-1]
    x = stop[0]
    y = stop[-1]
    
    if a == x:
        for nums in range(b, y + 1):
            if elevation_map[a][nums] + delta >= 1:
                elevation_map[a][nums] += delta 
   
    elif b == y:
        for nums in range(a, x + 1):
            if elevation_map[nums][b] + delta >= 1:
                elevation_map[nums][b] += delta 
              

def get_average_elevation(elevation_map: List[List[int]]) -> float:
    """Return the average elevation across all cells in the elevation map
    elevation_map.

    Precondition: elevation_map is a valid elevation map.

    >>> get_average_elevation(UNIQUE_3X3)
    5.0
    >>> get_average_elevation(FOUR_BY_FOUR)
    3.8125
    """
    
    total = 0
    
    for nums in elevation_map:
        for digits in nums:
            total = total + digits
        
    return total / (len(elevation_map) * len(elevation_map))


def find_peak(elevation_map: List[List[int]]) -> List[int]:
    """Return the cell that is the highest point in the elevation map
    elevation_map.

    Precondition: elevation_map is a valid elevation map.
                  Every elevation value in elevation_map is unique.

    >>> find_peak(UNIQUE_3X3)
    [1, 0]
    >>> find_peak(UNIQUE_4X4)
    [0, 3]
    """
    
    highest = 0
    
    for nums in elevation_map:
        for digits in nums:
            if digits > highest:
                highest = digits
                row = elevation_map.index(nums)
                position = nums.index(highest)
    
    return [row, position]


def is_sink(elevation_map: List[List[int]], cell: List[int]) -> bool:
    """Return True if and only if cell exists in the elevation map
    elevation_map and cell is a sink.

    Precondition: elevation_map is a valid elevation map.
                  cell is a 2-element list.

    >>> is_sink(THREE_BY_THREE, [0, 5])
    False
    >>> is_sink(THREE_BY_THREE, [0, 2])
    True
    >>> is_sink(THREE_BY_THREE, [1, 1])
    False
    >>> is_sink(FOUR_BY_FOUR, [2, 3])
    True
    >>> is_sink(FOUR_BY_FOUR, [3, 2])
    True
    >>> is_sink(FOUR_BY_FOUR, [1, 3])
    False
    """
    
    r = cell[0]
    c = cell[1]
    
    if (r < 0 or c < 0 or c > len(elevation_map) or r > len(elevation_map[0])):
        return False
    for num in range(c - 1, c + 2):
        for digit in range(r - 1, r + 2):
            if (num != -1 and digit != -1 and num < len(elevation_map) and \
                digit < len(elevation_map[r])):
                if elevation_map[digit][num] < elevation_map[r][c]:
                    return False
    return True
            
                        
def find_local_sink(elevation_map: List[List[int]],
                    cell: List[int]) -> List[int]:
    """Return the local sink of cell cell in elevation map elevation_map.

    Precondition: elevation_map is a valid elevation map.
                  elevation_map contains no duplicate elevation values.
                  cell is a valid cell in elevation_map.

    >>> find_local_sink(UNIQUE_3X3, [1, 1])
    [0, 0]
    >>> find_local_sink(UNIQUE_3X3, [2, 0])
    [2, 0]
    >>> find_local_sink(UNIQUE_4X4, [1, 3])
    [0, 2]
    >>> find_local_sink(UNIQUE_4X4, [2, 2])
    [2, 1]
    """
    
    r = cell[0]
    c = cell[1]
    lst = cell
    
    if (r < 0 or c < 0 or c > len(elevation_map) or r > len(elevation_map[0])):
        return False
    for num in range(c - 1, c + 2):
        for digit in range(r - 1, r + 2):
            if (num != -1 and digit != -1 and num < len(elevation_map) and \
                digit < len(elevation_map[r])):
                if elevation_map[digit][num] < elevation_map[lst[0]][lst[1]]:
                    lst[0] = digit
                    lst[1] = num
    return lst
    

def can_hike_to(elevation_map: List[List[int]], start: List[int],
                dest: List[int], supplies: int) -> bool:
    """Return True if and only if a hiker can go from start to dest in
    elevation_map without running out of supplies.

    Precondition: elevation_map is a valid elevation map.
                  start and dest are valid cells in elevation_map.
                  dest is North-West of start.
                  supplies >= 0

    >>> map = [[1, 6, 5, 6],
    ...        [2, 5, 6, 8],
    ...        [7, 2, 8, 1],
    ...        [4, 4, 7, 3]]
    >>> can_hike_to(map, [3, 3], [2, 2], 10)
    True
    >>> can_hike_to(map, [3, 3], [2, 2], 8)
    False
    >>> can_hike_to(map, [3, 3], [3, 0], 7)
    True
    >>> can_hike_to(map, [3, 3], [3, 0], 6)
    False
    >>> can_hike_to(map, [3, 3], [0, 0], 18)
    True
    >>> can_hike_to(map, [3, 3], [0, 0], 17)
    False

    """

    used = 0
    r = dest[0]
    c = dest[1]
    cr = start[0]
    cc = start[1]
    
    while (c < cc or r < cr):
        if (r == cr):
            used += abs(elevation_map[cr][cc] - elevation_map[cr][cc - 1])
            cc = cc - 1
        elif (c == cc):
            used += abs(elevation_map[cr][cc] - elevation_map[cr - 1][cc])
            cr = cr - 1
        else:
            if (abs(elevation_map[cr][cc] - elevation_map[cr][cc - 1]) \
                < abs(elevation_map[cr][cc] - elevation_map[cr - 1][cc])):
                used += abs(elevation_map[cr][cc] - elevation_map[cr][cc - 1])
                cc = cc - 1
            else:
                used += abs(elevation_map[cr][cc] - elevation_map[cr - 1][cc])
                cr = cr - 1  
    return used <= supplies
 

def get_lower_resolution(elevation_map: List[List[int]]) -> List[List[int]]:
    """Return a new elevation map, which is constructed from the values
    of elevation_map by decreasing the number of elevation points
    within it.

    Precondition: elevation_map is a valid elevation map.

    >>> get_lower_resolution(
    ...     [[1, 6, 5, 6],
    ...      [2, 5, 6, 8],
    ...      [7, 2, 8, 1],
    ...      [4, 4, 7, 3]])
    [[3, 6], [4, 4]]
    >>> get_lower_resolution(
    ...     [[7, 9, 1],
    ...      [4, 2, 1],
    ...      [3, 2, 3]])
    [[5, 1], [2, 3]]

    """
    
    r = c = 0
    temp = 0
    lst = []
    while (r < len(elevation_map)):
        lst.append([])
        while (c < len(elevation_map[0])):
            temp = 0
            if (c + 1 < len(elevation_map) and r + 1 < len(elevation_map[r])):
                temp += elevation_map[r][c] + elevation_map[r + 1][c] + \
                elevation_map[r][c + 1] + elevation_map[r + 1][c + 1]
                lst[int(r/2)].append(int(temp/4))
            elif (c + 1 < len(elevation_map)):
                temp += elevation_map[r][c] + elevation_map[r][c + 1] 
                lst[int(r/2)].append(int(temp/2))
            elif (r + 1 < len(elevation_map[r])):
                temp += elevation_map[r][c] + elevation_map[r + 1][c] 
                lst[int(r/2)].append(int(temp/2))
            else:
                temp += elevation_map[r][c]
                lst[int(r/2)].append(temp)
            c += 2
        r += 2
        c = 0
    return lst