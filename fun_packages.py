# This script shows some basic usage of my favourite packages
# This includes: Numba, Optuna, pydantic

# 1. Numba

# I really like this package, if you are running pure python operations in a function, numba is really great for 
# optimising it. The website says:
# Numba translates Python functions to optimized machine code at runtime using the industry-standard LLVM compiler library. 
# Numba-compiled numerical algorithms in Python can approach the speeds of C or FORTRAN.

from numba import njit
import numpy as np
import random

@njit
def monte_carlo_pi(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples

# it also makes parallelising really easy!

@njit(parallel=True)
def logistic_regression(Y, X, w, iterations):
    for i in range(iterations):
        w -= np.dot(((1.0 /
              (1.0 + np.exp(-Y * np.dot(X, w)))
              - 1.0) * Y), X)
    return w


# 2. Optuna

# Optuna is a powerful library for hyperparameter optimisation that allows you to automate the process of 
# tuning hyperparameters in machine learning models.

import optuna
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

def objective(trial):
    """Objective function to optimize."""
    # Suggest hyperparameters
    n_estimators = trial.suggest_int('n_estimators', 10, 100)
    max_depth = trial.suggest_int('max_depth', 1, 32)
    min_samples_split = trial.suggest_int('min_samples_split', 2, 20)

    # Create the model
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        random_state=42
    )

    # Fit the model
    model.fit(X_train, y_train)

    # Predict and evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    return accuracy  # Return the accuracy as the objective value

# Create the Optuna study
study = optuna.create_study(direction='maximize')  # We want to maximize accuracy
study.optimize(objective, n_trials=50)  # Optimize for 50 trials

# Print the best hyperparameters
print("Best hyperparameters: ", study.best_params)
print("Best accuracy: ", study.best_value)

# 3. pydantic

# Pydantic is a data validation and settings management library in Python that uses Python type annotations 
# to enforce data types and validate input data.

from pydantic import BaseModel, EmailStr, constr, ValidationError
from typing import List, Optional

class User(BaseModel):
    """Class to represent a user."""
    name: str
    age: int
    email: EmailStr  # Validates that the email is a valid email address
    bio: Optional[constr(max_length=300)] = None  # Optional field with a maximum length of 300 characters
    favorite_fruits: List[str]  # List of strings

# Example usage
try:
    user = User(
        name="Alice",
        age=30,
        email="alice@example.com",
        bio="Loves hiking and outdoor activities",
        favorite_fruits=["Apple", "Banana", "Cherry"]
    )
    print(user)
except ValidationError as e:
    print("Validation error:", e)

# Example of a user with invalid data
try:
    invalid_user = User(
        name="Bob",
        age=25,
        email="not-an-email",  # Invalid email
        favorite_fruits=["Mango"]
    )
except ValidationError as e:
    print("Validation error for invalid user:", e)
