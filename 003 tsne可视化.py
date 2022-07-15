####################
# 读取npz
####################

import numpy as np

doc = np.load('extract_output.npz')

extract_output = doc['extract_output']
y_test = doc['y_test']

print('extract_output.shape =', extract_output.shape)
print('y_test.shape =', y_test.shape)
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
x_tsne = tsne.fit_transform(extract_output)

####################
# visualization
####################

import matplotlib.pyplot as plt

# 绘制散点图
scatter = plt.scatter( x_tsne[:, 0], x_tsne[:, 1],
                       c=y_test, alpha=0.5,
                       marker='.' )

plt.title('visualization')
plt.tight_layout()
plt.show()
