import numpy as np
from neupy.algorithms import RBFKMeans
from mnist import MNIST

mnistData=MNIST('./mnistData')
imgTrain,lblTrain=mnistData.load_training()
imgTest,lblTest=mnistData.load_testing()
        

data = np.array(imgTrain)


rbfk_net = RBFKMeans(n_clusters=40, verbose=False)
rbfk_net.train(data, epsilon=1e-5)
print len(rbfk_net.centers)

new_data = np.array(imgTest[1])
print rbfk_net.predict(new_data).shape
