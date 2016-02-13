#!/usr/bin/env python3

# ---------------------------
# projects/Netflix/Netflix.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# -------
# imports
# -------

from pprint         import pprint
from math           import sqrt
from collections    import defaultdict
from time           import mktime
import json


# ----------------------
# set globals and caches
# ----------------------

movies = 17770
users = 480189
ratings = 100480507

output_data = {}

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

    return sqrt(se / len(actual))




# ------------
# netflix_eval
# ------------

def netflix_eval (movie_id, customer_id) :
    """
    movie_id the movie being rated
    customer_id the customer rating being predicted for a particular movie
    return the predicted value of the movie rating for the customer
    """

    global movie_averages

    return round(movie_averages[movie_id], 1)

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

#def netflix_solve (r, w) :
def netflix_solve (r, w) :
    """
    r a reader
    w a writer
    prints the predicted scores and rmse for all movies and customers from reader
    """
    global output_data

    ratings = []
    movie = ''

    for line in r :
        # test if line is a movie id
        # if it is movie id, 
        # create a new key & list of ratings
        if ':' in line:
            movie = str(line).strip(':\n')
            ratings = []
            output_data[movie] = ratings


        # if it is not a movie id, call eval
        else:
            score = netflix_eval(str(movie), int(line))
            temp_list = [score]
            ratings = ratings + temp_list
            output_data[str(movie)] = ratings

    for key in sorted(output_data.keys()):
            netflix_print(w, str(key + ':'))
            #netflix_print(w, (str(output_data[key])))
            for value in output_data[str(key)]:
                netflix_print(w, str(value))
        