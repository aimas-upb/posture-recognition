'''
    Based on a novel by Mihai Trascau, famous author and scholar
'''
import matplotlib.pyplot as pp
import numpy as np
from sklearn import tree
from sklearn import cross_validation


class Example:
    '''Stores the name of a posture and a list of parameters set that exemplify that posture'''
    def __init__(self, posture, feature_vectors):
        print 'Building an example for', posture, 'with', len(feature_vectors), 'labels'
        ''' - posture is the name of the posture
            - vectors is a list of feature vectors'''
        self.posture = posture
        self.feature_vectors = feature_vectors

def input_data_of_examples(examples):
    '''given a list of Example objects returns two X,y for learning algorithms'''
    X = []
    y = []
    for e in examples:
        for features in e.feature_vectors:
            X.append(features)
            y.append(e.posture)
    
    return X,y


def filter_by_kl(feature_vectors):
    ''' filters the examples using divergence'''
    
    def normalize(vector):
        m = min(vector) - 10e-18
        vector = [v - m for v in vector]
        s = sum(vector)
        return [v / s for v in vector]
    
    def distance(index):
        p = normalize(feature_vectors[i])
        q = normalize(feature_vectors[i+1])
        #p = feature_vectors[i]
        #q = feature_vectors[i+1]
        
        return kl(p, q)
    
    distances = [distance(i) for i in range(len(feature_vectors) -1)]
    filtered = []
    print 'Got max:', max(distances), ', min:', min(distances), ', avg:', np.mean(distances), ' std:', np.std(distances)
    print 'Filtered', len(filtered), 'examples from initial', len(feature_vectors), 'examples'
    pp.plot(distances)
    pp.show()
     
    
      
    return [range(22)]
    
def kl(p, q):
    """Kullback-Leibler divergence D(P || Q) for discrete distributions
 
    Parameters
    ----------
    p, q : array-like, dtype=float, shape=n
        Discrete probability distributions.
    """
    
    idx = [i for i in range(len(p)) if p[i] != 0 and q[i] != 0]
    
    p = [p[i] for i in idx]
    q = [q[i] for i in idx]
    
    p = np.asarray(p, dtype=np.float)
    q = np.asarray(q, dtype=np.float)
 
    return np.sum(np.where(p != 0, p * np.log(p / q), 0))


def tree_classifier(examples):
    ''' Receives a list of Example objects and returns a tree.DecisionTreeClassifier'''
    X, y = input_data_of_examples(examples)
    print 'Having', len(X), 'example for', len(examples), 'classes'
    X_learn, X_test, y_learn, y_test = cross_validation.train_test_split(X, y) 
    
    print 'Learning from', len(X_learn), 'examples'    
    clf = tree.DecisionTreeClassifier()
    clf.fit(X_learn, y_learn)
    
    print 'Validating with', len(X_test), 'examples'
    score = clf.score(X_test, y_test)
    print 'Got score', score
    
    return clf
    