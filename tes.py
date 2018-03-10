import re  
import sys  
import os,glob  
  
#定义目录：目录下有多个文件需要处理  
path = 'D:\\working'  
#定义输出文件  
fout = open("tes.txt",'w')  

#改变路径  
os.chdir(path) 

filename = 'b'
fs = open(filename,'r+')  
#处理文件中的每一行数据  
for line in fs.readlines():  
    a = line.split()  
    '''
    if a != [] and a[0] in x:  
        fout.write(a[-1]+'\t')  
        if a[0] == 'gpgpu_n_param_mem_insn':  
            fout.write('\n')  
            break  
        '''
    if re.match('1',a[0]):
        fout.write(a[1]+'\n')
                  
fout.write('\n')    
fout.close()  