
import time 
import os

order = 1

rng = int(input(" enter the number of files ...  \n"))
path = str(input("the path : "))


# print("you have 5 seconds to focus on the specified dir ...\n")
# time.sleep(5);


for i in range(0,int(rng/4)) :    
    files = path + "/" + "0"+str(order)+"-pic.jpg" + " " + path + "/" + "0"+str(order+1)+"-pic.jpg" + " " + path + "/" + "0"+str(order+2)+"-pic.jpg" + " " + path + "/" + "0"+str(order+3)+"-pic.jpg"
    

    folder_name = path + "/" + "0" + str(int(((order-1)/4)+1)) + "-folder" 

    os.system("mkdir " + folder_name)
    os.system("mv " + files + " " + folder_name + "/")
    order +=4

print("work done !")




