import os
import json
from skeleton_features import all_features, joints

#f = open("pos.txt")

top = ['player', 'created_at']
sensor_pos = ['X', 'Y', 'Z', 'alpha', 'beta', 'gamma']
valid_sensors = ['daq-01', 'daq-02', 'daq-03']


raw_data_path = '/home/ami/cosmin/proiecte/posture-recognition/raw-data-test'

def validJson(m):
    if (m['type'] != 'skeleton'):
        return False;
    elif (m['sensor_id'] not in valid_sensors):
        return False
    else:
        return True
    
def outputCsvFile(function, infileName, outfileName):
    print 'Processing file', infileName
    f = open(infileName)
    out = open(outfileName, 'w')
    for line in f:        
        if len(line.strip()) > 0:
            m = json.loads(line)
            if (validJson(m)):
                function(m, out)
    out.close()
    
def outputCsvLine(m, out):
    for j in joints:
        for p in ['X', 'Y', 'Z']:
            out.write(str(m['skeleton_3D'][j][p]))
            out.write(', ')
    out.write('\n') 

def outputFeaturesCsvLine(m, out):
    features = all_features(m['skeleton_3D'])
    for f in features:
        out.write(str(f))
        out.write(', ')
    out.write('\n') 


for f in os.listdir(raw_data_path):
    outputCsvFile(outputFeaturesCsvLine, raw_data_path + '/' + f, '/tmp/' + f + '.fts')
    