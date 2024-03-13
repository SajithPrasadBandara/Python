import os, shutil

#File Path
path = r"G:/Data Analysis/Python/Filesort/" 

#File List
files = os.listdir(path)  
 
#To check path is exists
os.path.exists(path + 'csv files') 

#Make folders name list
folder_names = ['PDF Files','CSV Files','Text Files','Images']

#Make folders
for x in range(0,4):
    if not os.path.exists(path + folder_names[x]):
        print(path + folder_names[x])
        os.makedirs(path + folder_names[x])
        

#Move files to relevant folder
for file in files:
    if '.csv' in file and not os.path.exists(path + "CSV Files/" + file):
        shutil.move(path + file,path +'CSV Files/' + file)
        
    elif '.pdf' in file and not os.path.exists(path + 'PDF Files/' + file):
        shutil.move(path + file,path + 'PDF Files/' + file)
        
    elif '.jpg' in file and not os.path.exists(path + 'Images/' + file):
        shutil.move(path + file,path +'Images/' + file)
        
    elif '.txt' in file and not os.path.exists(path + 'Text Files/' + file):
        shutil.move(path + file,path + 'Text Files/' + file)

 