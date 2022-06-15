import os 

path = fr'C:\Users\{os.getlogin()}\Documents\Articles'

file_name = 'zz results.txt'

os.chdir(path)

for folder in os.listdir(path):

    os.chdir(f'{path}/{folder}')


    if os.path.exists(file_name):
        os.remove(file_name)