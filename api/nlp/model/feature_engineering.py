from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import numpy as np


class FeatureEngineering:

    def percent_originality(self, lyric):

        tokens = word_tokenize(lyric, language='portuguese')
        response = len(set(tokens))/len(tokens)*100

        return round(response, 2)

    def total_words(self, lyric):

        tokens = word_tokenize(lyric, language='portuguese')
        response = len(tokens)

        return response

    def famous_word(self, lyric):
        tokens = word_tokenize(lyric, language='portuguese')

        freq_dist_tokens = FreqDist(tokens)
        word = freq_dist_tokens.most_common(1)
        
        return word[0][0]

    def split_train_test(self, df, ratio):
    
        indices = np.random.permutation(len(df))
        test_set_size = int(len(df) * ratio)
        valid_indices = indices[:test_set_size]
        train_indices = indices[test_set_size:]

        return df.iloc[train_indices], df.iloc[valid_indices]