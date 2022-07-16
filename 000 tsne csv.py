####################
# 读取csv
####################

f = open('Irisesquanted.csv')
lines = f.readlines()
f.close()

data = []

# PhenoID
# BlueGray	DarkBrown	Green	LightBrown

for line in lines[1:]:
    line = line.replace('\n', '').split(',')
    data.append( list(map(float, line[1:])) )

import numpy as np
data = np.array(data)
print('data.shape =', data.shape)
print()

####################
# tsne
####################

from sklearn.manifold import TSNE

tsne = TSNE( n_components=2,
             learning_rate='auto',
             # init='pca',
             init='random',
             )

x_tsne = tsne.fit_transform(data)

####################
# dbscan
####################

from sklearn.cluster import DBSCAN

clustering = DBSCAN( eps=3, # 样本间最小距离
                     min_samples=5, # 最小样本数
                     ).fit(x_tsne)

color = clustering.labels_

classes = np.unique(color)
print('classes =', classes)
print('len(classes) =', len(classes))

####################
# visualization
####################

import matplotlib.pyplot as plt

# 绘制散点图
scatter = plt.scatter( x_tsne[:, 0], x_tsne[:, 1],
                       alpha=0.5, c=color, cmap='jet', 
                       marker='.' )

# auto legend
plt.legend( *scatter.legend_elements(prop='colors'),
            title='iris', loc='best' )

plt.title('dbscan & tsne')
plt.tight_layout()
plt.show()
