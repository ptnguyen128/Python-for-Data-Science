import pandas as pd

# If you'd like to try this lab with PCA instead of Isomap,
# as the dimensionality reduction technique:
Test_PCA = True


def plotDecisionBoundary(model, X, y):
  print "Plotting..."
  import matplotlib.pyplot as plt
  import matplotlib
  matplotlib.style.use('ggplot') # Look Pretty

  fig = plt.figure()
  ax = fig.add_subplot(111)

  padding = 0.1
  resolution = 0.1

  from matplotlib.colors import ListedColormap
  cmap_light = ListedColormap(['#AAFFAA', '#AAAAFF'])
  cmap_bold  = ListedColormap(['#00AA00', '#0000AA'])
  
  # Calculate the boundaries
  x_min, x_max = X[:, 0].min(), X[:, 0].max()
  y_min, y_max = X[:, 1].min(), X[:, 1].max()
  x_range = x_max - x_min
  y_range = y_max - y_min
  x_min -= x_range * padding
  y_min -= y_range * padding
  x_max += x_range * padding
  y_max += y_range * padding

  # Create a 2D Grid Matrix. The values stored in the matrix
  # are the predictions of the class at said location
  import numpy as np
  xx, yy = np.meshgrid(np.arange(x_min, x_max, resolution),
                       np.arange(y_min, y_max, resolution))

  # What class does the classifier say?
  Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
  Z = Z.reshape(xx.shape)

  # Plot the contour map
  plt.contourf(xx, yy, Z, cmap=cmap_light)
  plt.axis('tight')

  # Plot our original points as well...
  for label in np.unique(y):
    #label: (2 for benign, 4 for malignant)
    c = 0 if label==2 else 1
    indices = np.where(y == label)
    plt.scatter(X[indices, 0], X[indices, 1], c=cmap_bold(c), alpha=0.8)

  p = model.get_params()
  plt.title('K = ' + str(p['n_neighbors']))
  plt.show()


# 
# TODO: Load in the dataset into a variable called 'X'.
# Identify nans, and set proper headers.
# Be sure to verify the rows line up by looking at the file in a text editor.
#
# .. your code here ..
X = pd.read_csv('/Users/superpup/Documents/edxpython/Module5KNN/Datasets/breast-cancer-wisconsin.data', header=None)
X.columns = ['sample', 'thickness', 'size', 'shape', 'adhesion', 'epithelial', 'nuclei', 'chromatin', 'nucleoli', 'mitoses', 'status']

# 
# TODO: Copy out the status column into a slice, then drop it from the main
# dataframe. You can also drop the sample column, since that doesn't provide
# us with any machine learning power.
#
# .. your code here ..
status = X['status'].copy()
X = X.drop(['status','sample'],1)
X = X.apply(lambda X: pd.to_numeric(X,errors = 'coerce'))

#
# TODO: With the labels safely extracted from the dataset, replace any nan values
# with the mean feature / column value
#
# .. your code here ..
X = X.fillna(X.mean())

#
# TODO: Experiment with the basic SKLearn preprocessing scalers. We know that
# the features consist of different units mixed in together, so it's reasonable
# to assume feature scaling is necessary. Print out a description of the
# dataset, post transformation.
#
# .. your code here ..
from sklearn import preprocessing
X = preprocessing.normalize(X)

#
# PCA and Isomap are your new best friends
model = None
if Test_PCA:
  print "Computing 2D Principle Components"
  #
  # TODO: Implement PCA here. save your model into the variable 'model'.
  # You should reduce down to two dimensions.
  #
  # .. your code here ..
  from sklearn.decomposition import PCA
  pca = PCA(n_components=2)
  pca.fit(X)
  model = pca.transform(X)

else:
  print "Computing 2D Isomap Manifold"
  #
  # TODO: Implement Isomap here. save your model into the variable 'model'
  # Experiment with K values from 5-10.
  # You should reduce down to two dimensions.
  #
  # .. your code here ..
  from sklearn import manifold
  iso = manifold.Isomap(n_neighbors=4, n_components=2)
  iso.fit(X)
  model = iso.transform(X)


#
# TODO: Train your model against X and transform it. You can save the results
# right back into X itself.
#
# .. your code here ..




#
# TODO: Do train_test_split. Use the same variable names as on the EdX platform in
# the reading material, but set the random_state=7 for reproducibility, and keep
# the test_size at 0.33 (33%).
#
# .. your code here ..
from sklearn.cross_validation import train_test_split
data_train, data_test, label_train, label_test = train_test_split(model, status, test_size=0.33, random_state=7)

# 
# TODO: Implement and train KNeighborsClassifier on your projected 2D
# training data here. You can use any K value from 1 - 15, so play around
# with it and see what results you can come up. Your goal is to find a
# good balance where you aren't too specific (low-K), nor are you too
# general (high-K). You should also experiment with how changing the weights
# parameter affects the results.
#
# .. your code here ..
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=15, weights = 'distance')
model.fit(data_train, label_train)
#
# INFO: Be sure to always keep the domain of the problem in mind! It's
# WAY more important to errantly classify a benign tumor as malignant,
# and have it removed, than to incorrectly leave a malignant tumor, believing
# it to be benign, and then having the patient progress in cancer. Since the UDF
# weights don't give you any class information, the only way to introduce this
# data into SKLearn's KNN Classifier is by "baking" it into your data. For
# example, randomly reducing the ratio of benign samples compared to malignant
# samples from the training set.



#
# TODO: Calculate + Print the accuracy of the testing set
#
# .. your code here ..
print model.score(data_test,label_test)

plotDecisionBoundary(model, data_test, label_test)


