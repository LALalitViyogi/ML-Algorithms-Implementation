
import pandas as pd 
import matplotlib.pyplot as plt 

data = pd.read_csv("/content/IRIS.csv")  ## Loading Iris dataset as dataframe

#=======================================================

setosa=data[data['species']=='Iris-setosa']           ## Data points which has Setosa as labels
versicolor=data[data['species']=='Iris-versicolor']## Data points which has Versicolor as labels
virginica =data[data['species']=='Iris-virginica'] ## Data points which has Verginica as labels

plt.figure()             
fig,ax=plt.subplots(1,1)  ## to plot all three labels in ax(same plot)

setosa.plot(x="sepal_length", y="sepal_width", kind="scatter",ax=ax,label='setosa',color='r')
versicolor.plot(x="sepal_length",y="sepal_width",kind="scatter",ax=ax,label='versicolor',color='b')
virginica.plot(x="sepal_length", y="sepal_width", kind="scatter", ax=ax, label='virginica', color='g')
plt.show()


fig,ax=plt.subplots(1,1)  ## Search how plt.subplots works for more understanding

setosa.plot(x="petal_length", y="petal_width", kind="scatter",ax=ax,label='setosa',color='r')
versicolor.plot(x="petal_length",y="petal_width",kind="scatter",ax=ax,label='versicolor',color='b')
virginica.plot(x="petal_length", y="petal_width", kind="scatter", ax=ax, label='virginica', color='g')

plt.show()
