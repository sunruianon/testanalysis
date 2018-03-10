import re  
import sys  
import os,glob  
import re

path = 'D:\\working'  #定义目录

fout = open("vmsis.txt",'w')  #定义输出文件  

os.chdir(path) #改变路径  

filename = 'a'
fs = open(filename,'r+',encoding='utf-8')  

for line in fs.readlines():  #处理文件中的每一行数据  
    a = line.split()  
    if a :
        if re.match('ffffffff',a[0]):
            if re.match('e8', a[1]):
                fout.write(a[0]+'\n')
    else:
        continue
    
                  
fout.write('\n')    
fout.close()  