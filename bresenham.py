#!/usr/bin/env python3

def get_line_points(pt1: ('x', 'y'), pt2: ('x', 'y')) -> [('x', 'y')]:
    """
    donne toutes les coordonnees de point entre pt1 et pt2 dans le sens de pt1 vers pt2
    """
    p1, p2 = ([None, None], [None, None])
    p1[0], p2[0], p1[1], p2[1] = (pt1[0], pt2[0], pt1[1], pt2[1])
    rev_dir = False
    rev_all = False
    direction = 1
    # on inverse X et Y si pas dans le bon sens
    if p1[1] > p2[1] or p1[0] == p2[0]:
        ty1, ty2 = p1[0], p2[0]
        p1[0], p2[0] = (p1[1], p2[1])
        p1[1], p2[1] = ty1, ty2
        rev_all = True
        direction = -1
    # on inverse X si pas dans le bon sens
    if p1[0] >= p2[0]:
        p1, p2 = (p2, p1)
        rev_dir = True
        if rev_all:
            direction = 1
    y = p1[1]
    # coeff directeur
    dy = p2[1] - p1[1]
    dx = p2[0] - p1[0]
    delta = dy / dx
    # pas incremental
    step = 0.0
    res = []
    for x in range(p1[0], p2[0] + 1):
        px, py = x, y
        if rev_all:
            px, py = y, x
        if rev_dir:
            res.insert(0, (px, py))
        else:
            res.append((px, py))
        step += delta
        if step >= 0.5:
            step -= 1.0
            y += direction
    return res

if __name__ == "__main__":
    import unittest

    class T(unittest.TestCase):
        def test(self):
            #ok
            self.assertEqual(get_line_points((0, 0), (5, 5)), [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
            #ok
            self.assertEqual(get_line_points((5, 5), (0, 0)), [(5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)])
            #ok
            self.assertEqual(get_line_points((0, 0), (0, 5)), [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5)])
            #ok
            self.assertEqual(get_line_points((0, 5), (0, 0)), [(0, 5), (0, 4), (0, 3), (0, 2), (0, 1), (0, 0)])
            #ok
            self.assertEqual(get_line_points((5, 0), (0, 0)), [(5, 0), (4, 0), (3, 0), (2, 0), (1, 0), (0, 0)])
            #ok
            self.assertEqual(get_line_points((0, 0), (5, 0)), [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0)])
    unittest.main()
