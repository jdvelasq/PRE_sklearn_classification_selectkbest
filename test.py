"""Classroom autograde script"""


def load_data():

    import pandas as pd

    dataset = pd.read_csv("heart_disease.csv")
    y = dataset.pop("target")
    x = dataset.copy()
    x["thal"] = x["thal"].map(
        lambda x: "normal" if x not in ["fixed", "fixed", "reversible"] else x
    )

    return x, y


def load_estimator():

    import os
    import pickle

    if not os.path.exists("estimator.pickle"):
        return None
    with open("estimator.pickle", "rb") as file:
        estimator = pickle.load(file)

    return estimator


def test():

    from sklearn.metrics import accuracy_score

    x, y = load_data()
    estimator = load_estimator()

    accuracy = accuracy_score(
        y_true=y,
        y_pred=estimator.predict(x),
    )

    assert accuracy > 0.8613


test()
