import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, \
                            f1_score, precision_score, recall_score
from sklearn.model_selection import cross_val_score

def displayScore(model, X, y, scoring, cv=5):
    scores = cross_val_score(model, X, y, cv=cv, scoring=scoring)
    print(f"=== {scoring.upper()}\n\
Mean:\t\t{scores.mean()}\n\
STD:\t\t{scores.std()}")

# Auxiliar function for metrics report
def metrics_report(model, X, y, y_true, y_pred):
    displayScore(model, X, y, "accuracy")
    displayScore(model, X, y, "precision")
    displayScore(model, X, y, "recall")
    displayScore(model, X, y, "f1")

# Auxiliar function for metrics report of ANN
def ann_metrics_report(ann, X, y, cv):
    l = len(y)
    results = list()
    for i in range(l//cv,l+1,l//cv):
        results.append(accuracy_score(y[i-l//cv:i], np.array(ann.predict(X[i-l//cv:i]) >= 0.5)))
    mean = sum(results) / cv
    var = sum([((res - mean) ** 2) for res in results]) / cv
    std = var ** (1/2)
    print(f"=== ACCURACY\n\
MEAN:\t\t{mean}\n\
STD:\t\t{std}")
