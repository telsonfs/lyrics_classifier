import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')

import re

from string import punctuation

class Preprocessing:


    def clean_word(self, lyric):

        response = lyric.replace('\n', ' ').replace("(", "").replace(")", "").replace('-', ' ').replace('/', ' ').replace('°', ' ').replace('+', ' ')
        response = re.sub(r'\[(.*)\]', '', response)
        response = re.sub(r'[0-9]', '', response)
        response = re.sub(r'[A-G]M\s', '', response)
        response = re.sub(r'[A-G]Mb\s', '', response)
        response = re.sub(r'[A-G]m\s', '', response)
        response = re.sub(r'[A-G]mb\s', '', response)
        response = re.sub(r'[A-G]\s', '', response)
        response = re.sub(r'[A-G]b\s', '', response)
        response = re.sub(r'[A-G]#\s', '', response)
        response = response.lower()
        
        return response

    def clean_lyric(self, lyrics):

        filtered_lyric = []
        outher_punctuation = ['...', '´´', '´', '``', '`', '..', '"', '. ..']       

        for lyric in lyrics:    
            lyric = self.clean_word(lyric)
            tokens = word_tokenize(lyric, language='portuguese')
            filtered_tokens = [word for word in tokens if not word in set(list(punctuation) + outher_punctuation + stopwords.words('portuguese'))]
            filtered_lyric.append(' '.join([word for word in filtered_tokens]))
            
        return filtered_lyric