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
from collections    import defaultdict
from time           import mktime
from numpy          import sqrt, subtract, mean, square
from collections    import OrderedDict
import json
import pickle
import os
import requests


# ----------------------
# set globals and caches
# ----------------------

movies = 17770
users = 480189
ratings = 100480507

output_data = OrderedDict()

with open('/u/downing/public_html/netflix-caches/ckc735-movies.json') as data_file:    
    movie_averages = json.load(data_file)

if os.path.isfile('/u/downing/public_html/netflix-caches/mdg7227-real_scores.pickle') :
    # Read cache from file system
    f = open('/u/downing/public_html/netflix-caches/mdg7227-real_scores.pickle','rb')
    real_scores = pickle.load(f)
else:
    # Read cache from HTTP
    bytes = requests.get('http://www.cs.utexas.edu/users/downing/netflix-caches/mdg7227-real_scores.pickle').content
    real_scores = pickle.loads(bytes)


# ------------
# netflix_rmse
# ------------

def netflix_rmse (actual, prediction) :
    """
    compute the root mean squared error between actual scores and predicted scores
    actual a list
    prediction a list
    return a decimal, representing the root mean squared error of predicted scores
    """

    return sqrt(mean(square(subtract(actual, prediction))))


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
# netflix_lookup
# -------------

def netflix_lookup (movie_id, customer_id) :
    """
    movie_id a string
    customer_id a string
    returns the actual score for a customer on a particular movie
    """

    global real_scores
    return real_scores[movie_id][customer_id]

# -------------
# netflix_solve
# -------------

def netflix_solve (r, w) :
    """
    r a reader
    w a writer
    prints the predicted scores and rmse for all movies and customers from reader
    """
    global output_data
    global real_scores

    pred_ratings = []
    actual_ratings = []
    movie = ''

    for line in r :
        # test if line is a movie id
        # if it is movie id, 
        # create a new key & list of ratings
        if ':' in line:
            movie = str(line).strip(':\n')

            pred_ratings = []
            actual_ratings = []
            


        # if it is not a movie id, call eval
        else:

            customer = int(str(line).strip('\n'))

            # Look up actual & predicted score from cache
            predicted_score = [netflix_eval(str(movie), customer)]
            actual_score = [real_scores[int(movie.strip(':'))][customer]]


            # build list of predicted and actual ratings
            pred_ratings = pred_ratings + predicted_score
            actual_ratings = actual_ratings + actual_score
            
            # output_data.pop(movie)
            output_data[movie] = [actual_ratings, pred_ratings]
    
    z1 = []
    z2 = []

    for key in sorted(output_data.keys()):


        z1 += (output_data[str(key)][0])
        z2 += (output_data[str(key)][1])


        netflix_print(w, str(key + ':'))

        for value in output_data[str(key)][1]:
            netflix_print(w, str(value))



    rmse = netflix_rmse(z1, z2)
    netflix_print(w,str("RMSE: " + str(round(rmse,2))))


        

