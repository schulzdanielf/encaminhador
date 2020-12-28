import pandas as pd
import pickle
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import sklearn
import re
import numpy as np
nltk.download('punkt')
nltk.download('stopwords')

class Classificador():

    def classifica(action):
        with open('alarmes/classificador/label_encoder', 'rb') as training_model:
            le = pickle.load(training_model)
        with open('alarmes/classificador/count_vectorizer', 'rb') as training_model:
            vectorizer = pickle.load(training_model)
        with open('alarmes/classificador/tfidf_converter', 'rb') as training_model:
            tfidfconverter = pickle.load(training_model)
        with open('alarmes/classificador/text_classifier', 'rb') as training_model:
            classifier = pickle.load(training_model)
        #Capturando o hostname
        inicio = action.index('Host')
        fim = inicio + action[inicio:].index('\n')
        hostname = action[inicio+6:fim]
        #Capturando a mensagem
        inicio = action.index('Mensagem')
        fim = inicio + action[inicio:].index('\n')
        mensagem = action[inicio+10:fim]
        #Tokenização
        token = word_tokenize(mensagem.lower())
        #Adicionando Hostname como último token
        token.append(hostname.lower())
        #Criando dicionário de STOP WORDS da língua portugues
        stop_words = set(stopwords.words('portuguese'))
        #Acrescentando valores identificados na frequência de distribuição
        stop_words.update(('-', ':', '(', ')', '%', ',', '.', '=', '..', '>', '?', '[', ']', '/', '2020', '', '&', '90', '!', 'to', 'in', '95.00', '--', ';', '<', 'c', 'nan', '1', '00', '10', 'estabelecido', 'acima', '#'))
        #Remove tokens desnecessários com expressões regulares
        regex = '^([\s\d]+)$'
        date_time_regex = '(\d{4})-(\d{2})-(\d{2})'
        date_regex = '(\d{4})/(\d{2})/(\d{2})'
        date_regex2 = '(\d{2})/(\d{2})'
        date_regex3 = '(\d{2})-(\d{2})-(\d{4})'
        date_regex4 = '(\d{2})_(\d{2})_(\d{2})'
        perc_regex = '(\d{2})\.(\d{2})'
        perc_regex2 = '(\d{2}),(\d{2})'
        for j in range(len(token)):
        #       token[j] = token[j].split('=')[0]
            if(re.findall(date_time_regex, token[j]) != []):
                token[j] = '%'
            if(re.findall(date_regex, token[j]) != []):
                token[j] = '%'
            if(re.findall(date_regex2, token[j]) != []):
                token[j] = '%'
            if(re.findall(date_regex3, token[j]) != []):
                token[j] = '%'
            if(re.findall(date_regex4, token[j]) != []):
                token[j] = '%'
            if((re.findall(perc_regex, token[j]) != []) & (len(token[j]) < 10)):
                token[j] = '%'
            if((re.findall(perc_regex2, token[j]) != []) & (len(token[j]) < 10)):
                token[j] = '%'
            if(re.findall(regex, token[j]) != []):
                token[j] = '%'
            token[j] = token[j].split(':')[0]
        #Removendo Stop Words
        token = [word for word in token if word not in stop_words]
        #Agrupa os tokens
        array = []
        array.append(' '.join(token))
        #Cria array vetorizado com tfidf
        array = vectorizer.transform(array).toarray()
        array = tfidfconverter.transform(array).toarray()
        #Retorna a previsão
        probs = classifier.predict_proba(array)
        best_n = np.argsort(probs, axis = 1)[:,-1:]
        return best_n[0]
