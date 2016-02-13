#!/usr/bin/env python3

# ---------------------------
# projects/Netflix/Netflix.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# ------------
# Netflix_read
# ------------

def Netflix_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# Netflix_eval
# ------------

def Netflix_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    # <your code>
    return 1

# -------------
# Netflix_print
# -------------

def Netflix_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# Netflix_solve
# -------------

def Netflix_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = Netflix_read(s)
        v    = Netflix_eval(i, j)
        Netflix_print(w, i, j, v)