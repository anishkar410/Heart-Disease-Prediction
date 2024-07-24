# -*- coding: utf-8 -*-
"""heartdiseaseprediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LHC8rHxtCNvXnTYfDHzvStbRiyuOiRTw
"""

import pandas as pd  # Importing pandas for data manipulation
import numpy as np  # Importing numpy for numerical operations
import seaborn as sns  # Importing seaborn for data visualization
import matplotlib.pyplot as plt  # Importing matplotlib for plotting
from sklearn import preprocessing  # Importing preprocessing module from sklearn for data normalization
from sklearn.model_selection import train_test_split  # Importing train_test_split for splitting data into training and testing sets
from sklearn.linear_model import LogisticRegression  # Importing LogisticRegression model from sklearn
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report  # Importing metrics for model evaluation

# Load the dataset
disease_df = pd.read_csv("/content/framingham.csv")  # Reading CSV file into a DataFrame

# Initial data exploration
print(disease_df.head())  # Displaying the first few rows of the dataset
print("Shape of the dataset:", disease_df.shape)  # Printing the shape of the dataset (rows, columns)
print("Value counts of TenYearCHD:")  # Displaying the count of unique values in 'TenYearCHD'
print(disease_df.TenYearCHD.value_counts())

# Data preprocessing
# Drop 'education' column and rename 'male' to 'Sex_male'
disease_df.drop(columns=['education'], inplace=True)  # Dropping the 'education' column as it's not needed
disease_df.rename(columns={'male': 'Sex_male'}, inplace=True)  # Renaming 'male' column to 'Sex_male' for clarity

# Handle missing values by removing rows with NaN values
disease_df.dropna(inplace=True)  # Dropping rows with any missing values

# Verify data after cleaning
print(disease_df.head())  # Displaying the first few rows of the cleaned dataset
print("Shape of the dataset after cleaning:", disease_df.shape)  # Printing the shape after cleaning
print("Value counts of TenYearCHD after cleaning:")  # Displaying value counts after cleaning
print(disease_df.TenYearCHD.value_counts())

# Visualization of the target variable distribution
plt.figure(figsize=(7, 5))  # Setting the figure size
sns.countplot(x='TenYearCHD', data=disease_df, palette="Spectral")  # Plotting count of 'TenYearCHD' values
plt.title('Count of TenYearCHD Values')  # Setting plot title
plt.show()  # Displaying the plot

# Line plot to visualize the TenYearCHD column
plt.figure(figsize=(10, 6))  # Setting the figure size
plt.plot(disease_df.index, disease_df['TenYearCHD'], color='blue', linestyle='-', marker='o', markersize=2, linewidth=0.5)  # Plotting TenYearCHD values over index
plt.title('TenYearCHD Values Over Index')  # Setting plot title
plt.xlabel('Index')  # Labeling x-axis
plt.ylabel('TenYearCHD')  # Labeling y-axis
plt.show()  # Displaying the plot

# Feature selection and target variable assignment
features = ['age', 'Sex_male', 'cigsPerDay', 'totChol', 'sysBP', 'glucose']  # Selecting relevant features for the model
X = np.asarray(disease_df[features])  # Converting selected features to numpy array
y = np.asarray(disease_df['TenYearCHD'])  # Converting target variable to numpy array

# Normalization of the dataset
X = preprocessing.StandardScaler().fit_transform(X)  # Normalizing the features

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=4)  # Splitting data into training and testing sets

print('Train set shape:', X_train.shape, y_train.shape)  # Printing shape of the training set
print('Test set shape:', X_test.shape, y_test.shape)  # Printing shape of the testing set

# Logistic Regression Model
logreg = LogisticRegression()  # Initializing the Logistic Regression model
logreg.fit(X_train, y_train)  # Training the model on the training data
y_pred = logreg.predict(X_test)  # Making predictions on the test data

# Evaluation and accuracy
accuracy = accuracy_score(y_test, y_pred)  # Calculating accuracy of the model
print('Accuracy of the model is =', accuracy)  # Printing the accuracy

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)  # Generating confusion matrix
conf_matrix = pd.DataFrame(cm, columns=['Predicted:0', 'Predicted:1'], index=['Actual:0', 'Actual:1'])  # Creating a DataFrame for the confusion matrix

plt.figure(figsize=(8, 5))  # Setting the figure size
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap="YlGnBu")  # Plotting the confusion matrix
plt.title('Confusion Matrix')  # Setting plot title
plt.show()  # Displaying the plot

# Classification report
print('Details for confusion matrix:')  # Printing a message before displaying the classification report
print(classification_report(y_test, y_pred))  # Displaying the classification report with precision, recall, f1-score