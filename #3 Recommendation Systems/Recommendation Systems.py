# recommendation systems learn by going to through of out history, learn what we like, then recommend relevant services 
# There are two main types of recommender systems 1: collaborative systems	2: content-based systems
# This script will recomend a movie a user will like 

# we will use three dependancies
		# Numpy
		# Scipy
		#LightFM

# importing dependancies
import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

# warp ( Weighted aproximate ranked pairwise), it's a hybrid system

#fetch dataset and format it 

data = fetch_movielens(min_rating=4.0)

print(repr(data['train']))
print(repr(data['test']))

#creat model

model = LightFM(loss='wrap')

#train the model

model.fit(data['train'],epochs=30, num_threads=2)

## to be continued 