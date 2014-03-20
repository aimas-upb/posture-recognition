'''
    Based on a novel by Mihai Trascau, famous author and scholar
'''
from sklearn import tree


class Example:
    '''Stores the name of a posture and a list of parameters set that exemplify that posture'''
    def __init__(self, posture, feature_vectors):
        print 'Building an example for', posture, 'with', len(feature_vectors), 'labels'
        ''' - posture is the name of the posture
            - vectors is a list of feature vectors'''
        self.posture = posture
        self.feature_vectors = feature_vectors

def tree_classifier(examples):
    ''' Receives a list of Example objects and returns a tree.DecisionTreeClassifier'''
    X = []
    y = []
    for e in examples:
        for features in e.feature_vectors:
            X.append(features)
            y.append(e.posture)

    print 'Using', len(y), 'example for', len(examples), 'classes' 

    clf = tree.DecisionTreeClassifier()
    clf.fit(X, y)
    print clf.score(X, y)
    return clf
    