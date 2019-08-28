#!/usr/bin/python                                                                                                                                                               
                                                                                                                                                                                
import shutil                                                                                                                                                                   
import os, sys                                                                                                                                                                  
                                                                                                                                                                                
list_of_files_to_copy = ['filename', 'filename','filename','folder/filename']                                                                   
src = "/folder/folder/folder"                                                                                                                         
dst = "/home/ec2-user/folder/"                                                                                                                                             
                                                                                                                                                                                
for f in list_of_files_to_copy:                                                                                                                                                 
    try:                                                                                                                                                                        
        print('Trying to copy: %s'%(src+f))                                                                                                                                     
        shutil.copy(src+f, dst)                                                                                                                                                 
        print('Copied')                                                                                                                                                         
    except:                                                                                                                                                                     
    print('FAILED!!!')                                                                                                                                                      
                                                                                                                                                                                
prntDst = os.listdir(dst)                                                                                                                                                       
print 'Destination Dir after copy operation: '                                                                                                                                  
print(prntDst)   
