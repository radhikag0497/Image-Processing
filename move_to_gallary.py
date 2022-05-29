import glob
import shutil
import os
import sys

def main(arg):
    
    src_dir = os.path.join(r'<path/of/your/source/dir>',arg)
    print('Source Directory:',src_dir)
    dst_dir = r'<path/of/your/destination/dir>'
    
    for jpgfile in glob.iglob(os.path.join(src_dir, "*.jpg")):
        shutil.copy(jpgfile, dst_dir)
        print('Copied file {} to Gallary'.format(jpgfile))

if __name__=="__main__":
    # if this script is called by some other script, receive the name from other script as argument
    # main(sys.argv[1])
    # pass the name to rename all image files of same person with iterator. 
    main('Narendra Modi')
