
import numpy as np
import xlrd
import matplotlib.pyplot as plt
doc = xlrd.open_workbook('Data\SouthAfricanHeartDiseaseFixed.xlsx').sheet_by_index(0)
#the history column has been moved into last position

attributeNames = doc.row_values(rowx=0, start_colx=1, end_colx=11) 
#all the column Names

FamHistory = doc.col_values(10,1,463) 
HistoryType = sorted(set(FamHistory))
HistoryDict = dict(zip(HistoryType,range(len(HistoryType))))
#Transformed Family History into integers

y = np.array([HistoryDict[value] for value in FamHistory])
#the array with integers instead of strings

X = np.empty((462,9))
for i in range(0,9):
    X[:,i] = np.array(doc.col_values(i+1,1,463)).T
    #the whole table except the first and last column
    
N = len(y)
M = len(attributeNames)
C = len(HistoryType)
#we will need those

X_c = X.copy()
y_c = y.copy()
attributeNames_c = attributeNames.copy()
#copies of our variables

alldata=np.concatenate((X_c, np.expand_dims(y_c,axis=1)), axis=1)
#complete matrix with all the data


chdlabels=doc.col_values(9,1,463)
chdTypeflo = sorted(set(chdlabels))
chdType=[int(i) for i in chdTypeflo]
chdType[1]='sick'
chdType[0]='healthy'

y_r=alldata[:, 2]
X_r=alldata[:,[0,1,3,4,5,6,7,8,9]]

i = 1; j = 2;
color = ['g','r']
plt.title('Heart disease insidents')
for c in range(len(chdType)):
    idx = y_c == c
    plt.scatter(x=X_c[idx, i],
                y=X_c[idx, j], 
                c=color[c], 
                s=20, alpha=0.5,
                label=chdType[c])
plt.legend(chdType)
plt.xlabel(attributeNames_c[i])
plt.ylabel(attributeNames_c[j])
plt.show()


