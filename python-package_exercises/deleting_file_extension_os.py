import os
path="D:\\"
for x in os.listdir(path):
    #print(x)
    if x.endswith('.jpeg'):
        print(x)
        #os.unlink(path+x)
        print("file deleted")