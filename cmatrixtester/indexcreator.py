# make an in index of all the templates/images along with their paths and their respective classification (true)
# path 	filename	class
import os
import shutil
import time
count = 0
start_time = time.time()
parentPath = 'wkdir' #change this to desired folder path 
print('1 for template index creation') #can change this (hardcode)
print('2 for image index creation') # can change this (hardcode)
mode = input()

if(mode == '1'):
	fname = 'template.txt' #change this to desired file name
	txtfile = open(fname,'w')
	for root, dirs, files in os.walk(parentPath): 
		for file in files:
			if 'Template' in file: #change if you are following a different naming convention
				print('templateaae')
				
				path_file = os.path.join(root,file)
				count=count + 1
				content = str(path_file+'\t'+file+'\t'+path_file.split(os.sep)[-2]+'\n')
				print(content)
				txtfile.write(content)
elif (mode == '2'):
	fname = 'index.txt' #change this to desired file name
	txtfile = open(fname,'w')
	for root, dirs, files in os.walk(parentPath): 
		for file in files:
			if 'Template' not in file: #change if you are following a different naming convention
				print('templateaae')
				
				path_file = os.path.join(root,file)
				count=count + 1
				content = str(path_file+'\t'+file+'\t'+path_file.split(os.sep)[-2]+'\n')
				print(content)
				txtfile.write(content)


print("--- %s seconds ---" % (time.time() - start_time))
print('count: ', count)
