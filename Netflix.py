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
from time           import mktime
from numpy          import sqrt, subtract, mean, square
from collections    import OrderedDict
import json
import pickle
import os
import requests

# ------------
# get_pickle
# ------------

def get_pickle (filepath) :
    """
    Accept a file patch to a .pickle cache file and return a dict
    filepath a string
    return a loaded pickle object
    """

    answer = {}

    if os.path.isfile('/u/downing/public_html/netflix-caches/' + filepath) :
    # Read cache from file system
        f = open('/u/downing/public_html/netflix-caches/' + filepath,'rb')
        answer = pickle.load(f)
        f.close()
    else: # pragma no cover
    # Read cache from HTTP
        bytes = requests.get('http://www.cs.utexas.edu/users/downing/netflix-caches/' + filepath).content
        answer = pickle.loads(bytes)

    return answer


# ----------------------
# set globals and caches
# ----------------------

output_data = OrderedDict()
movie_averages = {}
customer_avg = get_pickle('kh549-customer_average.pickle')
real_scores = get_pickle('mdg7227-real_scores.pickle')
offsets = get_pickle('shp425-avg_offsets.pickle')

with open('/u/downing/public_html/netflix-caches/ckc735-movies.json') as data_file:    
   movie_averages = json.load(data_file)





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
    evaluate the predicted score of a customer for a movie
    movie_id the movie being rated
    customer_id the customer rating being predicted for a particular movie
    return the predicted value of the movie rating for the customer taken by the average rating for a movie minus the average offset
    """

    global movie_averages
    # global real_scores
    global avg_offsets

    # total_offset = 0
    # num_movies = 0

    # for movie in real_scores:
    #     if customer_id in real_scores[movie]:
    #        total_offset += (movie_averages[str(movie)] - real_scores[movie][customer_id])
    #        num_movies += 1

    # avg_offset = total_offset / num_movies

    return round(movie_averages[movie_id] - avg_offsets[customer_id], 1)

# -------------
# netflix_print
# -------------

def netflix_print (w, i) :
    """
    print one line of text to buffer
    w a writer
    i the movie_id or the predicted score
    """
    w.write(str(i) + "\n")

# -------------
# netflix_zip
# -------------

def netflix_zip (output_data, w) :
    """
    Align two data sets for RMSE
    output_data a dict
    w a writer
    returns two lists of corresponding actual and predicted values
    """
    z1 = []
    z2 = []

    for key in sorted(output_data.keys()):


        z1 += (output_data[str(key)][0])
        z2 += (output_data[str(key)][1])


        netflix_print(w, str(key + ':'))

        for value in output_data[str(key)][1]:
            netflix_print(w, str(value))

    return z1, z2



# -------------
# netflix_solve
# -------------

def netflix_solve (r, w) :
    """
    predict the scores for a list of movies and customers then compute the RMSE
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
    z1, z2 = netflix_zip(output_data, w)
    rmse = netflix_rmse(z1, z2)
    w.write(str("RMSE: " + str(round(rmse,2))))

        

