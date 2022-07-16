f = open('Irisesquanted.csv')
lines = f.readlines()
f.close()

name_color_dict = {}

# PhenoID
# BlueGray	DarkBrown	Green	LightBrown

for line in lines[1:]:
    line = line.replace('\n', '').split(',')
    name_color_dict[int(line[0])] = list(map(float, line[1:]))

# 打印前十个
for i in list(name_color_dict.items())[:10]:
    print(i)
print()

####################
# 读取测试
# 有些问题，csv不全，有些文件名找不到
####################

import os
files = os.listdir('iris_224/')

for i in files:
    if i.split('.')[-1] == 'png':
        try:
            i = int(i.split('_')[0])

            name_color_dict[i]
            # print( name_color_dict[i] )
        except:
            print(i, end=',')
