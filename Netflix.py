#!/usr/bin/env python3

# ---------------------------
# projects/Netflix/Netflix.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# -------
# imports
# -------

from json           import load
from pprint         import pprint
from math           import sqrt
from collections    import defaultdict

with open('/u/fares/public_html/netflix-tests/ckc735-movies.json') as data_file:    
    movie_averages = json.load(data_file)


# ------------
# netflix_rmse
# ------------

def netflix_rmse (actual, prediction) :
    """
    compute the root mean squared error between actual scores and predicted scores
    a a list
    p a list
    return a decimal, representing the root mean squared error of predicted scores
    """

    # zip two lists into a list of tuples with corresponding values
    z = zip(actual, prediction)
    # the squared error
    se = 0

    for x, y in z:
        d = x - y
        ds = d**2
        se += ds

    return sqrt(se / len(z))

# ------------
# get_mse
# ------------

def netflix_rmse (actual, prediction) :
    """
    compute the root mean squared error between actual scores and predicted scores
    a a list
    p a list
    return a decimal, representing the root mean squared error of predicted scores
    """     


# ------------
# netflix_read
# ------------

def netflix_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# netflix_eval
# ------------

def netflix_eval (movie_id, customer_id) :
    """
    movie_id the movie being rated
    customer_id the customer rating being predicted for a particular movie
    return the predicted value of the movie rating for the customer
    """
    # <your code>
    return 1

# -------------
# netflix_print
# -------------

def netflix_print (w, i) :
    """
    print one line of text
    w a writer
    i the movie_id or the predicted score
    """
    w.write(str(i) + "\n")

# -------------
# netflix_solve
# -------------

def netflix_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = netflix_read(s)
        v    = netflix_eval(i, j)
        netflix_print(w, i, j, v)