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

from Netflix import netflix_eval, netflix_print, netflix_solve, netflix_rmse, netflix_zip

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :

    def setUp (self) :
        self.a = [
            netflix_eval,
            netflix_print,
            netflix_solve,
            netflix_rmse,
            netflix_zip]

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        with self.subTest():
            v = netflix_eval('1', 10)
            self.assertEqual(v, 3.6)

    def test_eval_2 (self) :
        with self.subTest():
            v = netflix_eval('10017', 2280428)
            self.assertEqual(v, 2.9)

    def test_eval_3 (self) :
        with self.subTest():
            v = netflix_eval('4310', 2523970)
            self.assertEqual(v, 3.6)



    # ----
    # rmse
    # ----

    def test_rmse_1 (self) :
        with self.subTest():
            v = netflix_rmse([1,2,3], [2,1,4])
            self.assertEqual(v, 1)

    def test_rmse_2 (self) :
        with self.subTest():
            v = netflix_rmse([1,1,1], [2,2,2])
            self.assertEqual(v, 1)

    def test_rmse_3 (self) :
        with self.subTest():
            v = netflix_rmse([2,2,2], [1,1,1])
            self.assertEqual(v, 1)

    def test_rmse_4 (self) :
        with self.subTest():
            v = netflix_rmse([5, 5, 5], [4, 4, 4])
            self.assertEqual(v, 1)


    # -----
    # print
    # -----

    def test_print_1 (self) :
        with self.subTest():
            w = StringIO()
            netflix_print(w, '10:')
            self.assertEqual(w.getvalue(), "10:\n")

    def test_print_2 (self) :
        with self.subTest():
            w = StringIO()
            netflix_print(w, '10')
            self.assertEqual(w.getvalue(), "10\n")

    def test_print_3 (self) :
        with self.subTest():
            w = StringIO()
            netflix_print(w, '1')
            self.assertEqual(w.getvalue(), "1\n")


    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        with self.subTest():
            r = StringIO("1:\n30878\n2647871\n1283744\n")
            w = StringIO()
            netflix_solve(r, w)
            self.assertEqual(w.getvalue(), "1:\n3.9\n3.5\n3.7\nRMSE: 0.5")

    def test_solve_2 (self) :
        with self.subTest():
            r = StringIO("1:\n30878\n2647871\n1283744\n10:\n1952305\n1531863\n")
            w = StringIO()
            netflix_solve(r, w)
            self.assertEqual(w.getvalue(), "1:\n3.9\n3.5\n3.7\n10:\n3.1\n2.6\nRMSE: 0.43")

    # -----
    # zip
    # -----

    def test_zip_1 (self) :
        with self.subTest():
            w = StringIO()
            z1 = []
            z2 = []

            test_output = {'test' : [[1], [1]]}
            z1, z2 = netflix_zip(test_output, w)

            self.assertEqual(z1, [1])
            self.assertEqual(z2, [1])

    def test_zip_2 (self) :
        with self.subTest():
            w = StringIO()
            z1 = []
            z2 = []

            test_output = {'test' : [[2, 2], [1, 1]]}
            z1, z2 = netflix_zip(test_output, w)

            self.assertEqual(z1, [2, 2])
            self.assertEqual(z2, [1, 1])

    def test_zip_3 (self) :
        with self.subTest():
            w = StringIO()
            z1 = []
            z2 = []

            test_output = {'test' : [[2, 2, 3], [1, 1, 2]]}
            z1, z2 = netflix_zip(test_output, w)

            self.assertEqual(z1, [2, 2, 3])
            self.assertEqual(z2, [1, 1, 2])


# ----
# main
# ----

if __name__ == "__main__" :
    main()

""" # pragma no cover
% coverage3 run --branch TestNetflix.py     > TestNetflix.out 2>&1



% coverage3 report -m --omit='/lusr/lib/python3.4/dist-packages/*' >> TestNetflix.out



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