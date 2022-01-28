import numpy as np
from time import time
from sklearn import metrics
from sklearn.model_selection import cross_val_score

from sklearn.ensemble import BaggingClassifier, RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

class Metrics:

    def benchmark(self, clf, x_train, y_train, x_test, y_test):
        print('_' * 80)
        print("Training: ")
        print(clf)
        t0 = time()
    
        clf.fit(x_train, y_train)
        train_time = time() - t0
        print("train time: %0.3fs" % train_time)

        t0 = time()
        pred = clf.predict(x_test)
        test_time = time() - t0
        print("test time:  %0.3fs" % test_time)        

        score = metrics.f1_score(y_test, pred, average='micro')
        #matrix = metrics.confusion_matrix(y_test, pred)
        report = metrics.classification_report(y_test, pred)
        print("f1_score:   %0.3f" % score)
        print("*************** Classification Report ***************")
        print(report)
        print("Confusion Matrix")
        print()

        return clf


    def experiments_models(self, genre, text_vect):
        k = 10
        
        results = {
            'model': ['BaggingClassifier', 'RandomForestClassifier', 'LogisticRegression', 'KNeighborsClassifier', 'DecisionTreeClassifier'],
            'score': []
        }
        
        scores = cross_val_score(BaggingClassifier(), text_vect, genre, cv = k)
        score = np.mean(scores)
        results['score'].append(score)
        print(f"BaggingClassifier: {score}")
        print('=' * 80)
        
        scores = cross_val_score(RandomForestClassifier(), text_vect, genre, cv = k)
        score = np.mean(scores)
        results['score'].append(score)
        print(f"RandomForestClassifier: {score}")
        print('=' * 80)
        
        scores = cross_val_score(LogisticRegression(), text_vect, genre, cv = k)
        score = np.mean(scores)
        results['score'].append(score)
        print(f"LogisticRegression: {score}")
        print('=' * 80)

        scores = cross_val_score(KNeighborsClassifier(), text_vect, genre, cv = k)
        score = np.mean(scores)
        results['score'].append(score)
        print('=' * 80)
        print(f"KNeighborsClassifier: {score}")
        
        scores = cross_val_score(DecisionTreeClassifier(), text_vect, genre, cv = k)
        score = np.mean(scores)
        results['score'].append(score)
        print('=' * 80)
        print(f"DecisionTreeClassifier: {score}")

        return results