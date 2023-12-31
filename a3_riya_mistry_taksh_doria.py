# -*- coding: utf-8 -*-
"""A3-Riya-Mistry-Taksh-Doria.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tZz8TlP-5GelyJVASQDfx5UQREq5P8MQ

<h1><center>CSCI 4146/6409 - Process of Data Science (Summer 2023)</center></h1>
<h1><center>Assignment 3</center></h1>

<b>Taksh Vijaybhai Doria</b>
B00918135


<b>Riya Dipakbhai Mistry</b>
B00931939

<h1>1. Data Prepration:</h1>
"""



import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
import numpy as np

data=pd.read_csv('/creditcard.csv')
data = data.dropna()

data

"""<h3>d. Divide the dataset into features and targets. Detail your method and reasoning
behind it</h3>
"""

X=data.drop("Class",axis=1)
y=data["Class"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""Displaying Train,Test and Original dataset"""

print(X_train.head(),y_train.head())

print(X_test.head(),y_test.head())

data.head()

data.info()

"""From above observation we can say that all features are numeric and there are no missing values in any features.

<h3>b. Merge the Train and Original datasets. Provide a justification for this action.</h3>

Consistency: Keeping the datasets separate ensures that the training data remains consistent for the specific task of fraud detection.

Test integrity: Separating the datasets preserves the integrity of the Test dataset, allowing for accurate evaluation on unseen data.

Simplicity: Keeping the datasets separate simplifies the workflow and improves interpretability of the model.

Resource efficiency: Not merging the datasets helps manage computational resources efficiently, considering the potentially large size of the credit card fraud detection dataset.

<h3>c. Identify and remove any irrelevant features. Substantiate your choices. </h3>

There are no such features that can be considered as irrelevant in this dataset.

<h2> [2] Modeling and Understanding Ensemble Methods</h2>
<h3>[a] Train a baseline model using a single algorithm (e.g., a linear model such as
logistic regression) and assess its performance.</h3>

Here we have used Logistic Regression algorithm model to train the dataset as baseline model
"""

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model performance
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Print the evaluation metrics
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

"""<h3> [2b] Implement Bagging using a set of homogeneous models (e.g., Decision Trees).
Incrementally increase the number of models (from 1 to 10) and analyze the
impact on performance.</h3>
"""

# Define the maximum number of models
max_models = 5

# Initialize lists to store performance metrics
accuracy_list = []
precision_list = []
recall_list = []
f1_list = []

# Incrementally increase the number of models
for n_models in range(1, max_models + 1):
    # Initialize a BaggingClassifier with DecisionTree base estimator
    model = BaggingClassifier(estimator=DecisionTreeClassifier(), n_estimators=n_models, random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model's performance
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    # Append the performance metrics to the lists
    accuracy_list.append(accuracy)
    precision_list.append(precision)
    recall_list.append(recall)
    f1_list.append(f1)

# Print the performance metrics for each number of models
for n_models in range(1, max_models + 1):
    print("Number of Models:", n_models)
    print("Accuracy: {:.2f}%".format(accuracy_list[n_models - 1] * 100))
    print("Precision: {:.2f}%".format(precision_list[n_models - 1] * 100))
    print("Recall: {:.2f}%".format(recall_list[n_models - 1] * 100))
    print("F1 Score: {:.2f}%".format(f1_list[n_models - 1] * 100))
    print()

"""<h3> [2c] Implement Boosting, also using a set of homogeneous models. Similar to Bagging,
increase the number of models incrementally and observe the impact on
performance.</h3>
"""

max_models = 5

# Initialize lists to store performance metrics
accuracy_list = []
precision_list = []
recall_list = []
f1_list = []

# Incrementally increase the number of models
for n_models in range(1, max_models + 1):
    # Initialize an AdaBoostClassifier with DecisionTree base estimator
    model = AdaBoostClassifier(estimator=DecisionTreeClassifier(), n_estimators=n_models, random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model's performance
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    # Append the performance metrics to the lists
    accuracy_list.append(accuracy)
    precision_list.append(precision)
    recall_list.append(recall)
    f1_list.append(f1)

# Print the performance metrics for each number of models
for n_models in range(1, max_models + 1):
    print("Number of Models:", n_models)
    print("Accuracy: {:.2f}%".format(accuracy_list[n_models - 1] * 100))
    print("Precision: {:.2f}%".format(precision_list[n_models - 1] * 100))
    print("Recall: {:.2f}%".format(recall_list[n_models - 1] * 100))
    print("F1 Score: {:.2f}%".format(f1_list[n_models - 1] * 100))
    print()

"""<h2> 3. Hyperparameter Tuning and Model Quality Evaluation</h2>

<h3> [a] From the models you have developed in question/step 2, select one and proceed
with hyperparameter optimization. Discuss the selection of parameters you've
decided to tune and the range of values you are considering.</h3>

Here we have chosen implementation based on Bagging for our hyperparameter tuning.
Bagging with Decision Trees:

Number of estimators (n_estimators): This parameter determines the number of decision tree models to be aggregated. We can consider a range of values, such as [5,10, 15, 20].
Maximum depth of trees (max_depth): Tuning the maximum depth can help prevent overfitting. We can explore different values or use None for unlimited depth.
"""

base_estimator = DecisionTreeClassifier(random_state=42)
model = BaggingClassifier(estimator=base_estimator, random_state=42)

# Define the parameter grid for hyperparameter optimization
param_grid = {
    'n_estimators': [5,10,15, 20],  # Range of values to consider for n_estimators
    'base_estimator__max_depth': [None, 5, 10]  # Range of values to consider for max_depth
}

# Perform grid search for hyperparameter optimization
grid_search = GridSearchCV(model, param_grid, scoring='accuracy', cv=5)
grid_search.fit(X_train, y_train)

# Get the best hyperparameters
best_n_estimators = grid_search.best_params_['n_estimators']
best_max_depth = grid_search.best_params_['base_estimator__max_depth']

# Train the Bagging model with the best hyperparameters
base_estimator = DecisionTreeClassifier(max_depth=best_max_depth, random_state=42)
model = BaggingClassifier(estimator=base_estimator, n_estimators=best_n_estimators, random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Print the performance metrics
print("Number of Estimators:", best_n_estimators)
print("Max Depth:", best_max_depth)
print("Accuracy: {:.2f}%".format(accuracy * 100))
print("Precision: {:.2f}%".format(precision * 100))
print("Recall: {:.2f}%".format(recall * 100))
print("F1 Score: {:.2f}%".format(f1 * 100))

"""<h3> [b] Evaluate your optimized model using relevant metrics and graphical
representations (e.g., performance graphs). The selected metrics should effectively demonstrate the performance of the model as a function of the
hyperparameters. </h3>
"""

import matplotlib.pyplot as plt
import numpy as np

# Initialize empty lists to store performance metrics
n_estimators_values = [5,10,15,20]
accuracy_values = []

# Iterate over different values of n_estimators
for n_estimators in n_estimators_values:
    # Train the Bagging model with the optimized hyperparameters
    model = BaggingClassifier(estimator=DecisionTreeClassifier(max_depth=best_max_depth, random_state=42),
                              n_estimators=n_estimators, random_state=42)
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)

    # Append accuracy to the list
    accuracy_values.append(accuracy)

# Plot performance metrics as a function of n_estimators
#plt.figure(figsize=(10, 6))
#plt.plot(n_estimators_values, accuracy_values, marker='o')
#plt.xlabel('Number of Estimators')
#plt.ylabel('Accuracy')
#plt.title('Bagging with Decision Trees - Performance Metrics')
#plt.grid(True)
#plt.show()

"""<h2> 4.Predictions and Submission</h2>
<h4>a. Make predictions from the model that performed best in question/step 3. Also,
provide an analysis of the prediction results.
b. Reflect on your results, their implications, and any potential
improvements that could be implemented. </h4>

From the above figure it can be observed that as the number of estimators increases the accuracy decreases sharply and after some point it becomes constant. Also the model performs best when n_estimators=5 best fit.

Attached predictions.csv file contains the output of the prediction made by the model

"""

y_pred = model.predict(X_test)

# Store predictions in a CSV file
output_df = pd.DataFrame({'Predictions': y_pred})
output_df.to_csv('/predictions.csv', index=False)

