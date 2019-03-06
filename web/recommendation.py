import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from web.models import Songs,Ratings
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.metrics.pairwise import pairwise_distances 

def rmse(prediction, ground_truth):
    prediction = prediction[ground_truth.nonzero()].flatten() 
    ground_truth = ground_truth[ground_truth.nonzero()].flatten()
    return sqrt(mean_squared_error(prediction, ground_truth))

def Average(lst): 
    return sum(lst) / len(lst) 

def predict(ratings, similarity, type='user'):
    if type == 'user':
        mean_user_rating = ratings.mean(axis=1)
        ratings_diff = (ratings - mean_user_rating[:, np.newaxis])
        pred = mean_user_rating[:, np.newaxis] + similarity.dot(ratings_diff) / np.array([np.abs(similarity).sum(axis=1)]).T
    elif type == 'item':
        pred = ratings.dot(similarity) / np.array([np.abs(similarity).sum(axis=1)])
    return pred

def getResultUser(matrix,user_prediction,user_id):
    pred = user_prediction
    for i in range(0,5):
        max=-1;
        idx=-1;
        for x in range(0,len(matrix[0])-1):
            if matrix[user_id-1,x]==0:
                if pred[user_id-1,x]>max:
                    max=pred[user_id-1,x]
                    idx=x
        pred[user_id-1,idx]=0

def getResultItem(matrix,item_prediction,user_id):
    pred = item_prediction
    for i in range(0,5):
        max=-1;
        idx=-1;
        for x in range(0,len(matrix[0])-1):
            if matrix[user_id-1,x]==0:
                if pred[user_id-1,x]>max:
                    max=pred[user_id-1,x]
                    idx=x
        print(item.iat[idx,7])
        pred[user_id-1,idx]=0

def printResult(matrix,user_id):
	
	print("top 5 recommendations according to user-based collaborative filtering method")
	getResultUser(matrix,user_prediction,user_id)
    #print()
    #print("top 5 recommendations according to item-based collaborative filtering method")
    #getResultItem(matrix,item_prediction,user_id)

def recommender(user_id):
    ratings=pd.DataFrame(list(Ratings.objects.all().values()))
    items=pd.DataFrame(list(Songs.objects.all().values()))

    no_users = ratings.user_id.unique().shape[0]
    no_items = items.shape[0]

    users=[]
    stars=[]
    songs=[]
    for coln in ratings.itertuples():
        users.append(coln[4])
        songs.append(coln[3])
        stars.append(coln[2])

    matrix = np.zeros((no_users, no_items))
    for coln in ratings.itertuples():
    	users=coln[4]
    	items=coln[3]-1
    	matrix[users-1,items-1] = coln[2]

    user_sim = pairwise_distances(matrix, metric='cosine')
    #item_sim = pairwise_distances(matrix.T, metric='cosine')
    prediction = predict(matrix, user_sim, type='user')
    #item_prediction = predict(matrix, item_sim, type='item')

    print("top 5 recommendations according to user-based collaborative filtering method")
    print(prediction.shape)    

    pred=[]
    for i in range(0,prediction.shape[1]):
    	pred.append(prediction[user_id-1][i])

    rec_song=[]
    for i in range(0,8):
        max=-1;
        idx=-1;
        for x in range(0,len(pred)):
        	if pred[x]>max:
        		max=pred[x]
        		idx=x
        pred[idx]=0
        rec_song.append(idx)

    print(rec_song)
    
    print('User-based CF RMSE: ' + str(rmse(prediction,matrix)))
    #print('Item-based CF RMSE: ' + str(rmse(item_prediction,matrix)))

    return rec_song
