'''
    Based on a novel by Mihai Trascau, famous author and scholar
'''
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


