from __future__ import with_statement
import json, os
from os.path import basename, splitext

from posture_classifier import Example, tree_classifier
from skeleton_features import all_features

valid_sensors = ['daq-02']
#raw_data_path = '/home/liviu/proiecte/posture-recognition/raw-data'
raw_data_path = '/tmp/dateBune/grepped/final'


def example_from_file(filename, label = None):
    '''Returns an Experiment object reading exemple skeletons from an input file
       if label is None than the file name (w/o extension) is used
    '''
    
    print 'Processing file', filename
    if label is None:
        label = splitext(basename(filename))[0]
    
    with open(filename) as f:
        objects = [json.loads(line) for line in f]
        examples = [all_features(obj['skeleton_3D']) for obj in objects if validJson(obj)]
        return Example(label, examples[50 : -50])

def write_features_to_file(in_filename,out_filename):
    print 'Processing file', in_filename, 'to', out_filename
    
    with open(in_filename) as f, open(out_filename, 'w') as out:
        objects = [json.loads(line) for line in f]
        for obj in objects:
            if validJson(obj):
                for v in all_features(obj['skeleton_3D']):
                    out.write(str(v))
                    out.write(' ')
                out.write('\n')
                    
def main():
    def validFile(filename):
        return splitext(filename)[1] == '.txt'    

    if not os.path.isdir(raw_data_path):
        raise "%s is not a folder" % raw_data_path 

#     examples = [example_from_file(raw_data_path + '/' + filename) for filename in os.listdir(raw_data_path) if validFile(filename)]
#     classifier = tree_classifier(examples)    
#     print  classifier
    for filename in os.listdir(raw_data_path):
        if validFile(filename):
            write_features_to_file(raw_data_path + '/' + filename, '/tmp/1/' + splitext(basename(filename))[0] + '.mat')
    
def validJson(m):
    '''Returns true iff the json is of interest'''
    if (m['type'] != 'skeleton'):
        return False;
#     elif (m['sensor_id'] not in valid_sensors):
#         return False
    else:
        return True

if __name__ == "__main__":
    main()
