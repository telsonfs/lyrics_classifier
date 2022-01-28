from nltk.probability import FreqDist
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt


class Visualization:


    def freq_dist(self, words, n):
                
        freq_dist_tokens = FreqDist(words)
        freq_dist_tokens.most_common(n)
        
        # Grafico de distribuicao das palavras
        plt.figure()
        freq_dist_tokens.plot(n,cumulative=False)
        
        
    def word_cloud(self, text, genre):
        
        # gerar uma wordcloud
        wordcloud = WordCloud(background_color="black",
                            width=1600, height=800).generate(str(text))

        # mostrar a imagem final
        fig, ax = plt.subplots(figsize=(10,6))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.set_axis_off()

        plt.imshow(wordcloud)
        wordcloud.to_file("{genre}.png")