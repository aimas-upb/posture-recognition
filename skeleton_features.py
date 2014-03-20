import numpy.linalg
import math

joints = ['head', 'neck', 'left_shoulder', 'left_hand', 
          'left_knee', 'right_elbow', 'right_shoulder', 
          'right_hand', 'left_hip', 'right_hip', 'left_foot', 
          'left_elbow', 'torso', 'right_knee', 'right_foot']

triples = [ 
    ('head'            , 'neck'           , 'left_shoulder'),   
    ('head'            , 'neck'           , 'right_shoulder'),  
    ('neck'            , 'left_shoulder'  , 'left_elbow'),      
    ('neck'            , 'right_shoulder' , 'right_elbow'),     
    ('left_shoulder'   , 'left_elbow'     , 'left_hand'),       
    ('right_shoulder'  , 'right_elbow'    , 'right_hand'),      
    ('head'            , 'neck'           , 'torso'),           
    ('neck'            , 'torso'          , 'left_hip'),
    ('neck'            , 'torso'          , 'right_hip'),       
    ('torso'           , 'left_hip'       , 'left_knee'),       
    ('torso'           , 'right_hip'      , 'right_knee'),      
    ('left_hip'        , 'left_knee'      , 'left_foot'),       
    ('right_hip'       , 'right_knee'     , 'right_foot'),      
    ('neck'            , 'torso'          , 'left_knee'),       
    ('neck'		       , 'torso'          , 'right_knee')      
]


def radToDeg(rad):
    return rad / math.pi * 180

def vector_of_points(p2, p1):
    return [p2[0] - p1[0], p2[1]- p1[1], p2[2] - p1[2]]

def vector_angle_3d(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'    """
    cosang = numpy.dot(v1, v2)
    sinang = numpy.linalg.norm(numpy.cross(v1, v2))
    return numpy.arctan2(sinang, cosang)

def vector_to_xOy(p1, p2):
    v1 = vector_of_points(p1, p2)
    v2 = [0, 0, 1]#normal vector to the xOy plane
    
    return math.pi / 2 - vector_angle_3d(v1, v2)
    
def vector_to_yOz(p1, p2):
    v1 = vector_of_points(p1, p2)
    v2 = [1, 0, 0]#normal vector to the yOz plane
    
    return math.pi / 2 - vector_angle_3d(v1, v2)

def point_of_json(obj):
    """extracts a float vector from a json frament with X,Y,Z keys"""
    return [obj['X'], obj['Y'], obj['Z']]

def compute_angle_feature(triple, points):
    p1 = points[triple[0]]
    p2 = points[triple[1]]
    p3 = points[triple[2]]
    
    return vector_angle_3d(vector_of_points(p2, p1), vector_of_points(p3, p2)) 

def compute_angles(skeleton_3d):
    """expects a skeleotn 3d object as output by the AmI-Lab pipeline"""
    points = {}
    for j in joints:
        points[j] = point_of_json(skeleton_3d[j])
    
    inRad =  [compute_angle_feature(triple, points) for triple in triples]
    return [radToDeg(rad) for rad in inRad]
        
    