import shutil
import os
import commands

file_list = os.listdir('/home/website/CSC005/_posts/')
num, c_date = commands.getstatusoutput('date -d -7day +%Y-%m-%d')
print(c_date)

for f in file_list:
    f_date = f[0:10]
    print(f_date)
    if f_date == c_date:
        print(True)
        f_path = '/home/website/CSC005/_posts/' + f
        os.remove(f_path)

