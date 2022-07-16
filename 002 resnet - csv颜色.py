####################
# 读取图片
####################

import os
docs = os.listdir('iris_224/')
# print(docs)

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = []
color = []

# 甜甜圈
mask = [ [], [] ] # 需要采样的位置
for i in range(224):
    for j in range(224):
        dist = np.linalg.norm( np.array([112,112])-np.array([i,j]) )
        if dist <= 224/2 and dist >= 224/3/2:
            mask[0].append(i)
            mask[1].append(j)
mask = tuple(mask)
'''
plt.scatter(mask[0], mask[1])
plt.show()
'''


for i in docs: # 测试的时候少读一些 [:100]
    
    # img = mpimg.imread('iris_224/119_3.png')
    
    if i.split('.')[-1] == 'png': # 去掉不是图片的文件
        
        temp = mpimg.imread( 'iris_224/' + i )
        img.append( temp )
        
        color.append( np.mean(temp[mask], axis=0) ) # 统计颜色
        '''
        print( np.mean(temp[mask], axis=0) )
        print( temp[mask].shape )
        '''
        
    # img = img[np.newaxis, ...] # cnn增加新维度

img = np.array(img)
color = np.array(color)

# print()
# print()
print('img.shape = ', img.shape)
print('np.max(img) = ', np.max(img))
print('np.min(img) = ', np.min(img))
print()

print('color.shape =', color.shape)
print('np.max(color) = ', np.max(color, axis=0))
print('np.min(color) = ', np.min(color, axis=0))
print()

'''
plt.imshow(img)
plt.tight_layout()
plt.show()
'''

####################
# 避免占满
####################

os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'

####################
# 提取feature
####################

import tensorflow as tf

# imagenet大小是224*224 默认
resnet = tf.keras.applications.ResNet152V2(
    # include_top=True, # 默认，全连接层
    weights='imagenet'
    )
# print(resnet.summary())

extract_layer = tf.keras.Model( # 提取feature
    inputs = resnet.input, # 输入
    outputs = resnet.layers[-1].output # 维度1000的层
    )
'''
print(extract_layer.summary())
print()
'''

import time

time_a = time.time() # 计时

extract_output = extract_layer.predict(img)
print(extract_output.shape)

time_b = time.time() # 计时
print('time =', round(time_b-time_a, 4), 's')

####################
# 保存压缩npz
####################

np.savez_compressed( 'extract_output.npz',
                     extract_output = extract_output,
                     y_test = color )
