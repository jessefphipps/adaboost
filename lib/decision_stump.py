import pandas as pd
import numpy as np

class decision_stump_bubble_sort(D, x, y):
    for _ in range(0, len(x)):
        for i in range(0, len(x)-1):
            if x[i+1] < x[i]:
                x_tmp = x[i].copy()
                x[i] = x[i+1].copy()
                x[i+1] = x_tmp
                y_tmp = y[i].copy()
                y[i] = y[i+1].copy()
                y[i+1] = y_tmp
                D_tmp = D[i].copy()
                D[i] = D[i+1].copy()
                D[i+1] = D_tmp
    return D, x, y

class hypothesis:
    """
    --> The hypothesis class defines rules for a given classification for a weak classifier
    
    --> The threshold is the same dimension as any given input vector x.
    
    --> The polarization parameter defines which "side" of the threshold is labeled 1. Can be either 1 or -1.
    
    --> For example, if threshold = [4] and polarization = [-1], then this hypothesis states that any sample with 
    x0 < -4 should be labeled 1, and any sample with x0 >= -4 should be labeled 0.
    """
    def __init__(self, threshold, polarization, feature):
        self.feature = feature
        self.theshold_vector = threshold
        self.polarization_parameter = polarization

def decision_stump(D, x, y):
    """ 
    --> A decision stump is a weak classifier that produces a hypothesis given a 
    probability vector D, input vector x, and output vector y
    
    --> Currently, only a pandas dataframe is supported as an input for x. D and y must be list-like objects.
    """
    
    
    
    
    for feature in x.columns:
        D_feat, x_feat, y_feat = decision_stump_bubble_sort(D, x[feature], y)
        F = 0
        for 
        for b in [1, -1]:
            for n in range(0, len(x_feat)):
                
        