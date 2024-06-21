# -*- coding: utf-8 -*-
"""Untitled56.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aCn-dAMP2zpfjFRA2b_Ts5G58rJVbWKr
"""
from tqdm import tqdm
from bs4 import BeautifulSoup
from keybert import KeyBERT
from multi_rake import Rake
from summa import keywords
import re
import json
import yake
from gensim.summarization import keywords
from IPython.display import HTML
import pandas as pd
import requests
import os
import argparse
import spacy

from transformers import (
    TokenClassificationPipeline,
    AutoModelForTokenClassification,
    AutoTokenizer,
)
from transformers.pipelines import AggregationStrategy
import numpy as np
#import os
#os.environ['TRANSFORMERS_CACHE'] = 'E:\git\transformer_cache'

nlp = spacy.load("en_core_web_lg")


class keyword_extraction():
    def __init__(self, html_path, saving_path, method):
        self.html_path = html_path
        self.saving_path = saving_path
        self.method = method
        self.text = ''
        self.span_list = []

    
    def read_text_from_html(self):
        """uses beautifulsoup to read text from html files

        
        :returns: raw text from html
        :rtype: string

        """
        with open(self.html_path, encoding="utf-8") as f:
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')
            
            print(type(soup))
        self.soup = soup    
        
        
                #print(self.text)
        return self.soup
    
    def clean_up_html_to_text(self):
        self.extract_text_fom_html()
        #splitlines = self.soup.splitlines()
        #print(splitlines)
        #self.splitlines = splitlines
        
        print(type(self.text.splitlines()))

        '''with open(self.saving_path + 'text.txt', 'w', encoding="utf-8") as file:
                #text = self.text.replace("Final Government Distribution  Chapter 5 IPCC AR6 WGIII", "").replace("Final Government Distribution Chapter 5 IPCC AR6 WGIII", "")
                for line in tqdm(self.splitlines):
                    file.write(line)
                    
                print("Done Writing File")'''
        #return self.splitlines
               

    def extract_span_list(self):
        with open(self.html_path, 'r') as f:
            html = f.read()
            soup = BeautifulSoup(html, features="html.parser")
            with open('/content/html_ex.html', 'w', encoding="utf-8") as file:
                file.write(soup.prettify())
            # kill all script and style elements

            soup_elem = soup.find_all("span")
            for span_elem in soup_elem:
                # print(span_elem)
                span_elem.extract()
                span_text = span_elem.get_text().strip()
                lines = (line.strip() for line in span_text.splitlines())
                # break multi-headlines into a line each
                chunks = (phrase.strip() for line in lines for phrase in line.split("  ") if len(phrase.strip()) > 9)
                # drop blank lines
                # text_write = '\n'.join(chunk for chunk in chunks if chunk)
                span_text = ' '.join(chunk for chunk in chunks if chunk)
                if len(span_text) > 9 and 'http' not in span_text and 'doi' not in span_text and 'Chapter' not in span_text:
                    # print(span_text)
                    # print('-'*50)
                    self.span_list.append(span_text)
        return self.span_list
        # def tf_idf(self):

    '''def clean_text(self):
        self.extract_text_fom_html()
        f = self.text
        clean_t = self.text.replace("Final Government Distribution  Chapter 5 IPCC AR6 WGIII", "")
        return self.clean_t'''

    def clean(self, df):
        def tagger(x):
            return nlp(x)[0].pos_

        def lemma(x):
            # print(nlp(x)[0].lemma_)
            return nlp(x)[0].lemma_

        df['POS'] = df['keyword/phrase'].apply(lambda x: tagger(x))
        df['Lemma'] = df['keyword/phrase'].apply(lambda x: lemma(x))
        df = df[df['keyword/phrase'] == df['Lemma']]
        df = df.drop_duplicates(subset=['score'], keep='last')
        df = df[df.POS.isin(['NOUN', 'PROPN', 'ADJ', 'ADV'])]
        df = df[~df['keyword/phrase'].apply(lambda x: lemma(x)).isin(['http', 'https', 'publication', 'Chapter'])]
        df = df.drop(columns=['Lemma'], axis=0)
        return df

    def extract_text_fom_html(self):

        with open(self.html_path, 'r') as f:
            html = f.read()
            soup = BeautifulSoup(html, features="html.parser")

            for script in soup(["script", "style"]):
                script.extract()  # rip it out

            # get text
            text = soup.get_text()
            # print(text)
            # break into lines and remove leading and trailing space on each
            lines = (line.strip() for line in text.splitlines())
            # break multi-headlines into a line each
            chunks = (phrase.strip() for line in lines for phrase in line.split("      ") if len(phrase.strip()) > 9)
            # drop blank lines
            # text_write = '\n'.join(chunk for chunk in chunks if chunk)
            text = '\n '.join(chunk for chunk in chunks if chunk)
            self.text = text
            # print(text)
            # TEXT_ = f'Chapter06_text.txt'
            # saving_path = '/content/'
            with open(self.saving_path + 'text.txt', 'w', encoding="utf-8") as file:
                text = self.text.replace("Final Government Distribution  Chapter 5 IPCC AR6 WGIII", "").replace("Final Government Distribution Chapter 5 IPCC AR6 WGIII", "")
                for l in text.splitlines():
                    file.write(l+"\n \n \n")
                #file.write(text)
                print("Done Writing File")
                #print(self.text)
            return self.text

    def extract_text_fom_file(self):

        with open(self.text_file, 'r') as f:
            textv2 = f.read()

    def extract_keywords_rake(self):
        rake = Rake()
        self.extract_text_fom_html()
        keywords_Rake = rake.apply(self.text)
        df_Rake = pd.DataFrame(keywords_Rake)
        df_Rake.rename(columns={0: 'keyword/phrase', 1: 'score'}, inplace=True)
        df_Rake = self.clean(df_Rake)
        df_Rake.to_csv(self.saving_path + 'Rake_keywords.csv', index=None)

    def extract_keywords_gensim(self):
        self.extract_text_fom_html()
        keywords_gensim = keywords(self.text, words=100, scores=True, pos_filter=('NN', 'ADJ'), lemmatize=False,
                                   deacc=False)  # run over all parameters
        df_gensim = pd.DataFrame(keywords_gensim)
        df_gensim.rename(columns={0: 'keyword/phrase', 1: 'score'}, inplace=True)
        df_gensim = self.clean(df_gensim)
        df_gensim.to_csv(self.saving_path + 'gensim_keywords.csv', index=None)

    def extract_keywords_yake(self):
        self.extract_text_fom_html()
        kw_extractor = yake.KeywordExtractor(top=400, stopwords=None,)
        keywords_yake = kw_extractor.extract_keywords(self.text)
        df_yake =pd.DataFrame(keywords_yake)
        df_yake.rename(columns = {0:'keyword/phrase',1:'score'}, inplace = True)
        df_yake = self.clean(df_yake)
        df_yake['keyword/phrase'].to_csv(self.saving_path +'yake_keywords.csv',index=None) 

    def extract_keywords_textrank(self):
        self.extract_text_fom_html()
        keywords_textrank = keywords.keywords(self.text, scores=True)
        df_textrank = pd.DataFrame(keywords_textrank)
        df_textrank.rename(columns={0: 'keyword/phrase', 1: 'score'}, inplace=True)
        df_textrank = self.clean(df_textrank)
        df_textrank.to_csv(self.saving_path + 'textrank_keywords.csv', index=None)

    def extract_keywords_keyBERT(self):
        self.extract_text_fom_html()
        kw_model = KeyBERT(model='all-mpnet-base-v2')
        keywords_keyBERT = kw_model.extract_keywords(self.text,
                                                     keyphrase_ngram_range=(1, 3),
                                                     stop_words='english',

                                                     top_n=100)
        print(keywords_keyBERT)
    
    def extract_keywords_hf(self):
        self.keyphrases = []
        self.clean_up_html_to_text()
        model_name = "ml6team/keyphrase-extraction-kbir-inspec"
        for line in tqdm(self.text.splitlines()):
            #print(line) 

            extractor = KeyphraseExtractionPipeline(model=model_name)
            keyphrases = extractor(line)
            for i in keyphrases:
                self.keyphrases.append(i)
            #print(self.keyphrases)
        self.keyphrases = [*set(self.keyphrases)]
        df = pd.DataFrame(self.keyphrases)
        df.to_csv(self.saving_path + 'keyphrases.csv' ,index=False)
        return self.keyphrases
    
    def extraction_unigrams(self):

        df = pd.read_csv('Chapter05_keyphrases.csv')
        key = df['0'].tolist()
        unigram =[]
        ngram = []

        pattern = "\s"
        print(type(key))
        for i in key:
            if re.findall(pattern, i):
                ngram.append(i)
                #print('N-gram')
            else:
                unigram.append(i)
                #print('Unigram')
        #print(ngram)
        #print(unigram)
        #self.unigram = unigram
        print(len(unigram))
        return unigram
        #print(len(ngram))

    def wikidata_out(self):
        #list = self.extraction_unigrams()
        list = ['data']#, 'climate', 'mitigation']
        #list = self.unigram
        
        for i in list:
            self.wiki_lookup(i)
            json_object = json.dumps(self.result, indent=4)
            with open(self.saving_path + 'wikidata.txt', 'w', encoding="utf-8") as file:
                with open("sample.json", "w") as outfile:

                    outfile.write(json_object)


            

    

    def wiki_lookup(self, query):
        """Queries Wikidata API for Wikidata Item IDs for terms in ami-dict

        :param query: term to query wikdiata for ID
        :type query: string
        :returns: potential Wikidata Item URLs
        :rtype: list

        """
        params = {
            "action": "wbsearchentities",
            "search": query,
            "language": "en",
            "format": "json",
            "wbsprofile": "language"
        }
        data = requests.get(
            "https://www.wikidata.org/w/api.php", params=params)
        result = data.json()
        hit_list = []
        self.result = result
        for hit in result['search']:
            try:
                if "scientific article" not in hit["description"]:
                    hit_list.append(hit["id"])
            except:
                hit_list2.append(hit["id"])
        return hit_list



    def main(self):
        if method == 'rake':
            self.extract_keywords_rake()
        elif method == 'yake':
            self.extract_keywords_yake()
        elif method == 'gensim':
            self.extract_keywords_gensim()
        elif method == 'textrank':
            self.extract_keywords_textrank()
        elif method == 'keyBERT':
            self.extract_keywords_keyBERT()
       
        elif method == 'rawtext':
            self.wikidata_out()
        else :
            self.extract_keywords_hf()
        
class KeyphraseExtractionPipeline(TokenClassificationPipeline):
    def __init__(self, model, *args, **kwargs):
        super().__init__(
            model=AutoModelForTokenClassification.from_pretrained(model),
            tokenizer=AutoTokenizer.from_pretrained(model),
            *args,
            **kwargs
        )

    def postprocess(self, model_outputs):
        results = super().postprocess(
            model_outputs=model_outputs,
            aggregation_strategy=AggregationStrategy.SIMPLE,
        )
        return np.unique([result.get("word").strip() for result in results])
    



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--html_path',
                        required=False,
                        help=' path of the HTML file: /...')

    parser.add_argument('-t', '--text_file',
                        required=False,
                        help='path to textfile: /...')

    parser.add_argument('-s', '--saving_path',
                        required=True,
                        help='path of the folder where you want to save the files : /...'
                        )
    parser.add_argument('-m', '--method',
                        required=False, choices=['rake', 'yake', 'gensim', 'keyBERT', 'textrank', 'rawtext'],
                        help='which method you want to us to extact keywords (Default is HF Model) /...')
    parser.add_argument('--n_gram',
                        required=False,
                        type=int,
                        default=1,
                        help='length of n-grams to extract(Yake only) : /...'
                        )
    parser.add_argument('--html2text',
                        required=False,
                        action='store_true',
                        help='Converts HTML to TXT : /...'
                        )

    args = parser.parse_args()

    html_path = args.html_path  # '/content/semanticClimate/ipcc/ar6/wg3/Chapter06/fulltext.flow.html'
    saving_path = args.saving_path  # '/content/'
    method = args.method
    n_gram = args.n_gram
    text_file = args.text_file

    keyword_extractions = keyword_extraction(html_path, saving_path, method)
    keyword_extractions.main()
    if args.html2text:
        keyword_extractions.extract_text_fom_html()
    

    