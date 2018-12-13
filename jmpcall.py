import re  
import sys  
import os,glob  
import re

path = './'  #定义目录

fout = open("jmpcall.txt",'w')  #定义输出文件  

os.chdir(path) #改变路径  

filename = 'linux-4.20'
fs = open(filename,'r+',encoding='utf-8')  

pattern = re.compile('jmp|call')
pattern2 = re.compile('\*')

for line in fs.readlines():  #处理文件中的每一行数据  
    a = line.split()  
    if a :
        if pattern.search(line):
            if pattern2.search(line):
                    fout.write(line)
    else:
        continue
    
                  
fout.write('\n')    
fout.close()   
