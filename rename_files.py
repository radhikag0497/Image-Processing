'''
Here there are two codes
Code 1 : Renaming the downloaded files to the name of person fetched from end of path
mainly for files downloaded with single word name

Code 2 : Renaming files downloaded with two words name 
'''
import os, sys
import subprocess

# Absolute path of a file
directory = r'<path\of\dir>'

######### --- Code 1 --- ##########

# name = directory.split('/')[-1]
# # Renaming the file
# count = 0
# for file in os.listdir(directory):
#     print(file)
    
#     src = os.path.join(directory,file)
#     print('src',src)
#     rename = name+'-'+str(count)+'.jpg'
#     dest = os.path.join(directory,rename)
#     print('dest',dest)
#     count += 1
#     os.rename(src, dest)
    
# # move all file to face gallary
# os.system('python move_to_gallary.py '+name)

######### --- Code 2 --- ##########

# renaming the files with space between file names
def main(arg):
    # directory = os.path.join(r'<path\of\dir>',arg)

    count = 0
    for file in os.listdir(directory):
        if file.startswith(arg):
            print(file)
            
            src = os.path.join(directory,file)
            print('src',src)
            _name = arg.replace(' ', '_')
            rename = _name +'-'+str(count)+'.jpg'
            dest = os.path.join(directory,rename)
            print('dest',dest)
            count += 1
            os.rename(src, dest)
    # To call the move_to_gallary python script by passing the name of directory
    # os.system('python move_to_gallary.py '+_name)

if __name__=="__main__":
    # main(sys.argv[1])
    main('Amit Shah')
