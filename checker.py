#!/usr/bin/python
"""
checks that the stages have been completed, and creates the new clues
"""

import pickle
from PIL import Image, ImageDraw

state_file = '/tmp/.adventure_state'

root_dir = '/tmp/adventure/'

#stage 1 - check for 100 files
def check_stage_1():
    try:
        for file_num in range(1,2):
            file_name = root_dir + 'stage1/' + str(file_num)
            file_handle = open(file_name)
            lines = len(file_handle.readlines())
            if lines != file_num:
                raise Exception("wrong number of lines")
        print "passed"
        return True
    except Exception, e:
        print "failed", e 
        return False

def check_stage_2():
    try:
        file_name = root_dir + 'stage2/image.png'
        img = Image.open(file_name)
        colors = img.getcolors(10)
        count = 0
        for color in colors:
            if color[1] == (255,0,0):
                count +=1
            if color[1] == (0,255,0):
                count +=1
            if color[1] == (0,0,255):
                count +=1
        if count == 3:
            print "passed"
            return True
        else:
            print "failed"
            return False
    except Exception, e:
        print "failed", e

##################
try:
    stage = pickle.load(open(state_file))
except IOError:
    stage = 1

print "stage:", stage
if stage == 1:
    if check_stage_1():
        stage +=1
elif stage == 2:
    if check_stage_2():
        stage +=1

state_file = open(state_file,'w')
pickle.dump(stage,state_file)
