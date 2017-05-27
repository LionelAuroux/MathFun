#!/usr/bin/env python3

def getLine(pt1: ('x', 'y'), pt2: ('x', 'y')) -> [('x', 'y')]:
    direction = 1
    if pt1[0] >= pt2[0]:
        direction = -1
    dy = pt2[1] - pt1[1]
    dx = pt2[0] - pt1[0]
    e = 0.0
    e10 = dy / dx
    e01 = -1.0
    res = []
    y = pt1[1]
    for x in range(pt1[0], pt2[0], direction):
        res.append((x, y))
        e += e10
        if e >= 0.5:
            y += 1
            e += e01
    return res

if __name__ == "__main__":
    print("bresenham")
    r = getLine((0, 0), (10, 4))
    print(r)
