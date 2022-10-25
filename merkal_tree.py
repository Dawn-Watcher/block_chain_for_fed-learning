import hashlib
import os
def hash_data(data, hash_function = 'sha256'):
    "hash function"
    hash_function = getattr(hashlib, hash_function)
    data = data.encode('utf-8')
    return hash_function(data).hexdigest()

def concat_and_hash_list(lst, hash_function = 'sha256'):
    lst1 = []
    for i in lst:
        lst1.append(hash_data(i))
    
    
    assert len(lst1)>0, "no files"
    if len(lst1)==1:
        return lst1[0]
    elif len(lst1)==2:
        return hash_data(lst1[0]+lst1[1])
    
        
    n = 0 #merkle树高度
    while len(lst1) >1:
        n += 1
        if len(lst1)%2 == 0:
            v = []
            while len(lst1) >1 :
                a = lst1.pop(0)
                b = lst1.pop(0)
                v.append(hash_data(a+b, hash_function))
            lst1 = v
        else:
            v = []
            l = lst1.pop(-1)
            while len(lst1) >1 :
                a = lst1.pop(0)
                b = lst1.pop(0)
                v.append(hash_data(a+b, hash_function))
            v.append(l)
            lst1 = v
    return lst1

def preprocessing(path,pre_list): 
    read_dir(path,pre_list)
    return pre_list 

def read_dir(path,pre_list):
    files= os.listdir(path) 
    for file in files:
        file=os.path.join(path,file)

        if os.path.isfile(file):
            f = open(file); 
            iter_f = iter(f); 
            str = ""
            for line in iter_f: 
                str = str + line
            pre_list.append(hash_data(str))
        else:
            read_dir(file,pre_list)

def merkal(path):
    li=[]
    li=preprocessing(path,li)

    return concat_and_hash_list(li)


#merkal tree merkal为接口，使用绝对路径，可修改