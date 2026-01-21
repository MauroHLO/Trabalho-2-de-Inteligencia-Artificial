import numpy as np
from sklearn.datasets import make_moons, make_circles, load_iris

def get_duas_luas(n_samples=500, noise=0.05, random_state=42):
    X, y = make_moons(n_samples=n_samples, noise=noise, random_state=random_state)
    return X, y, ["x1", "x2"], ["moon_0", "moon_1"]

def get_dois_circulos(n_samples=500, noise=0.05, factor=0.5, random_state=42):
    X, y = make_circles(n_samples=n_samples, noise=noise, factor=factor, random_state=random_state)
    return X, y, ["x1", "x2"], ["circle_outer", "circle_inner"]

def get_iris():
    iris = load_iris()
    X = iris.data
    y = iris.target
    feature_names = iris.feature_names
    target_names = iris.target_names
    return X, y, feature_names, target_names