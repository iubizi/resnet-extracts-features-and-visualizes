'''
import os

files = os.listdir('iris/')

for file in files:
    
    try:
        name_list = file.split('_')
        new_name = name_list[0]+'_'+name_list[1]+name_list[-1][1:]
        print(name_list[-1])
        input()
        # print(new_name)
        os.rename('iris/'+file, 'iris/'+new_name)
    except:
        print('error!', file)
'''
