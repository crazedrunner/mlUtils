# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 11:56:51 2018

@author: crazedrunner
"""

import argparse
import datetime
import cv2
import os

def main():
    print('Entered main')
    ap = argparse.ArgumentParser()
    ap.add_argument('-s', '--source',type=str, help='Source of video files')
    ap.add_argument('-d', '--dest', type=str, help='Destination of output images')
    ap.add_argument('-b', '--stride', type=int, help='Stride detirements how frequently to grab a frame')
    ap.add_argument('-c', '--category', type=str, help='The name of the category, project, or class')
    args = vars(ap.parse_args())
    
    source = args['source']
    dest = args['dest']
    stride = args['stride']
    cat = args['category']
    
    print('Source: ', source)
    print('dest: ', dest)
    if cat is None:
        cat = 'unk'
    if stride is None or stride < 1:
        stride = 1
    
    if source is None or dest is None:
        print('Must provide both source and destination')
        exit()
        
    if not os.path.isdir(dest):
        print('dest must be a directory')
        exit()
        
   
    if os.path.isdir(source):
        print('Entered directory flow')
        os.chdir(source)
        files = [f for f in os.listdir('./') if os.path.isfile(f)]
        for file in files:
            grab_frames(file, dest, stride, cat)
    else:
        grab_frames(source, dest, stride, cat)
        
                
def grab_frames(src, dest, stride, category):
	print('Entered grab_frames')
	counter = 0
	step = 0
	sFilename = os.path.basename(src)
	sFilename = sFilename.replace('.', '_')
	print(sFilename)
	path = os.path.abspath(dest)
	if path[:-1] != '\\' and path[:-1] != '/':
		path += '/'
	path += category + '/'
	if not os.path.exists(path):
		os.makedirs(path)
	video = cv2.VideoCapture(src)
	while video.isOpened():
		
		success, frame = video.read()
		if success: 
			if (step % stride) == 0 :
				filename = path + sFilename + '_' + format(counter, '06d') + '.jpg'
				print('[INFO] ' + str(datetime.datetime.now()) + ' Creating file: ' + filename)
				cv2.imwrite(filename,frame)
				counter += 1
		else:
			video.release()
		step += 1

if __name__== "__main__":
	main()