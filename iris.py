from matplotlib import pyplot as plt
from sklearn import datasets

def main():
    iris = datasets.load_iris()
    x = iris.data[:,:2]
    y = iris.target
    
    x_min, x_max = x[:,0].min() - .5, x[:,0].max() + .5
    y_min, y_max = x[:,1].min() - .5, x[:,1].max() + .5
    
    #plt.figure(2, figsize=(8,6))
    plt.clf()
    
    plt.scatter(x[:,0], x[:,1], c=y,cmap=plt.cm.Paired)
    plt.xlabel('Sepal length')
    plt.ylabel('Sepal width')
    plt.xlim(x_min,x_max)
    plt.ylim(y_min,y_max)
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()