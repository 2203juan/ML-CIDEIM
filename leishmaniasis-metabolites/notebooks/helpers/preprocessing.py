from sklearn.preprocessing import LabelEncoder
from sklearn.base import BaseEstimator, TransformerMixin

def encoding(df):
    le = LabelEncoder()
    df['y'] = le.fit_transform(df['y'])

class ParetoScaler(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.factors = None
        
    def fit(self, X, y=None):
        self.factors = {col:X[col].std()**(1/2) for col in X}
        return self
    
    def transform(self, X, y=None):
        X_ = X.copy()
        for col in X_:
            X_[col] /= self.factors[col]
        return X_
