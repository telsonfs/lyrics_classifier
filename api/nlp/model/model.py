import pickle


from nlp.model.preprocessing import Preprocessing

class Model:

    def vectorizer(self, model_vectorizer, column):
        
        model_vectorizer.fit(column)
        return model_vectorizer


    def save_model(self, clf, model_name):

        pickle.dump(clf, open(f"model/{model_name}.sav", "wb"))


    def lyric_classifier(self, lyric):
        preproc = Preprocessing()

        model_classifier = pickle.load(open('nlp/model/classifier.sav', 'rb'))
        model_vectorizer = pickle.load(open('nlp/model/vectorizer.sav', 'rb'))

        lyric = preproc.clean_lyric([lyric])

        lyric_vect = model_vectorizer.transform(lyric)

        return model_classifier.predict(lyric_vect)