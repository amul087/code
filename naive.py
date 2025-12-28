 Naive Bayes Spam Filter

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv("dataset.csv")

# Clean dataset
dataset.dropna(inplace=True)


X = dataset.iloc[:, 0].values
y = dataset.iloc[:, 1].values


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

cv = CountVectorizer()
X = cv.fit_transform(X).toarray()


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0
)

# Train Naive Bayes Classifier
from sklearn.naive_bayes import MultinomialNB

classifier = MultinomialNB()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

compare = np.vstack((y_test, y_pred)).T
print(compare)


from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
print(cm)


correct = 0
incorrect = 0
for i in range(len(y_pred)):
    if y_pred[i] == y_test[i]:
        correct += 1
    else:
        incorrect += 1

print("Correct predictions:", correct)
print("Incorrect predictions:", incorrect)
print("Accuracy of the Naive Bayes Classification is:", correct / len(y_pred))
