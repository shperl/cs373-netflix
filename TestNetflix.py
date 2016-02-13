#!/usr/bin/env python3

# -------------------------------
# projects/Netflix/TestNetflix.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Netflix import netflix_eval, netflix_print, netflix_solve, netflix_rmse

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = netflix_eval('1', 10)
        self.assertEqual(v, 3.8)

    def test_eval_2 (self) :
        v = netflix_eval('10', 200)
        self.assertEqual(v, 3.2)


    # ----
    # rmse
    # ----

    def test_rmse_1 (self) :
        v = netflix_rmse([1,2,3], [2,1,4])
        self.assertEqual(v, 1)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        netflix_print(w, '10:')
        self.assertEqual(w.getvalue(), "10:\n")

    def test_print_2 (self) :
        w = StringIO()
        netflix_print(w, '10')
        self.assertEqual(w.getvalue(), "10\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1:\n1000\n1001\n1002\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "1:\n3.8\n3.8\n3.8\n")

# ----
# main
# ----

if __name__ == "__main__" :
    main()

""" # pragma no cover
% coverage3 run --branch TestNetflix.py >  TestNetflix.out 2>&1



% coverage3 report -m                   >> TestNetflix.out



% cat TestNetflix.out

.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s
OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Netflix          18      0      6      0   100%
TestNetflix      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""