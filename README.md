# resnet-extracts-features-and-visualizes

resnet extracts features and visualizes

## 方法

使用resnet来提取feature，这里使用的是152层的resnet，第二个版本，使用imagenet来提取feature，维度是1000的fc层

之后可视化，使用tsne来看分布情况

## 可视化结果

001 使用resnet152v2提取iris的feature，之后进行tsne可视化

![resnet152v2](https://github.com/iubizi/resnet-extracts-features-and-visualizes/blob/main/resnet152v2.PNG)

002 使用dbscan和tsne可视化经过颜色筛选的csv数据

![dbscan](https://github.com/iubizi/resnet-extracts-features-and-visualizes/blob/main/dbscan.PNG)
