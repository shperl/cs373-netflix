#!/usr/bin/env python3

# ------------------------------
# projects/Netflix/RunNetflix.py
# Copyright (C) 2016
# Glenn P. Downing
# ------------------------------

# -------
# imports
# -------

import sys

from Netflix import netflix_solve

# ----
# main
# ----

if __name__ == "__main__" :
    netflix_solve(sys.stdin, sys.stdout)



"""
% cat RunNetflix.in
1:
30878
2647871
1283744
2488120
317050
1904905
1989766
14756
1027056
1149588
1394012
1406595
2529547
1682104
2625019
2603381
1774623
470861
712610
1772839
1059319
2380848
548064
10:
1952305
1531863



% RunNetflix.py < RunNetflix.in > RunNetflix.out



% cat RunNetflix.out
1:
3.8
3.8
3.8
3.8
3.8
3.8
3.8
3.8
3.8
3.8
3.8
3.8
3.8
3.8
3.8
3.8
3.8
3.8
3.8
3.8
3.8
3.8
3.8
10:
3.2
3.2
RMSE: .8



% pydoc3 -w Netflix
# That creates the file Netflix.html
"""