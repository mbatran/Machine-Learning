from sklearn import svm

# Write our variable as a list of lists

#length, wigth, shoe size
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

#labels categorical list
y=['male','female','female','female','male','male',
'male','female','male','female','male']

# initialize classifier
clf=svm.SVC()

# train the classifier
clf.fit(X, y)

#predict a new value 
predition = clf.predict([[190,70,43]])

# print the new value

print(predition)
