import matplotlib.pyplot as pp
 
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

def cluster(features_vectors):
    features_vectors = StandardScaler().fit_transform(features_vectors)
    db = DBSCAN(eps=0.3, min_samples=10).fit(features_vectors)
    core_samples = db.core_sample_indices_
    labels = db.labels_

    # Number of clusters in labels, ignoring noise if present.
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    
#     print 'Clusters', n_clusters, 'labels', labels
    
    
    pp.plot(labels)
    pp.show()
    
    
    