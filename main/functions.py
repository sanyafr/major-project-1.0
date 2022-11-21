import PyPDF2

import nltk


#function to parse, no need actually
def extract_text_from_pdf(example):
    #inbuilt function
    # creating a pdf file object
    pdfFileObj = open(r'example', 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # printing number of pages in pdf file
    print(pdfReader.numPages)

    # creating a page object
    pageObj = pdfReader.getPage(0)

    # extracting text from page
    return (pageObj.extractText())


#nlkt built in functions
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


#function to extract names, resume text passed as argument
def extract_names(txt):
    #array for all the names
    person_names = []
    #tokenizing the whole text
    for sent in nltk.sent_tokenize(txt):

        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            #identifying the entities according to label
            if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
                # if it matches adding to person names
                person_names.append(' '.join(
                    chunk_leave[0] for chunk_leave in chunk.leaves()))
#returning the names
    return person_names


#parsing resume text
#using above function to get names
# noqa: T001

#importing regex and subprocess
import re
import subprocess  # noqa: S404
#regex pattern for phone number
PHONE_REG = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')

#idk how this is done


#matching and returning the text that matches phone number regex pattern
def extract_phone_number(resume_text):
    phone = re.findall(PHONE_REG, resume_text)

    if phone:
        number = ''.join(phone[0])

        return number
    return None


#same as phone number
EMAIL_REG = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')


def extract_emails(resume_text):
    return re.findall(EMAIL_REG, resume_text)

# noqa: T001

nltk.download('stopwords')

# you may read the database from a csv file or some other database
SKILLS_DB = [
    'machine learning',
    'data science',
    'python',
    'word',
    'excel',
    'English',
]


def extract_skills(input_text):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    word_tokens = nltk.tokenize.word_tokenize(input_text)

    # remove the stop words
    filtered_tokens = [w for w in word_tokens if w not in stop_words]

    # remove the punctuation
    filtered_tokens = [w for w in word_tokens if w.isalpha()]

    # generate bigrams and trigrams (such as artificial intelligence)
    bigrams_trigrams = list(
        map(' '.join, nltk.everygrams(filtered_tokens, 2, 3)))

    # we create a set to keep the results in.
    found_skills = set()

    # we search for each token in our skills database
    for token in filtered_tokens:
        if token.lower() in SKILLS_DB:
            found_skills.add(token)

    # we search for each bigram and trigram in our skills database
    for ngram in bigrams_trigrams:
        if ngram.lower() in SKILLS_DB:
            found_skills.add(ngram)

    return found_skills


import requests

nltk.download('stopwords')

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

RESERVED_WORDS = [
    'school',
    'college',
    'univers',
    'academy',
    'faculty',
    'institute',
    'faculdades',
    'Schola',
    'schule',
    'lise',
    'lyceum',
    'lycee',
    'polytechnic',
    'kolej',
    'ünivers',
    'okul',
]

import re
import spacy
from nltk.corpus import stopwords

# load pre-trained model
nlp = spacy.load('en_core_web_sm')

# Grad all general stop words
STOPWORDS = set(stopwords.words('english'))

# Education Degrees
EDUCATION = [
    'BE', 'B.E.', 'B.E', 'BS', 'B.S', 'C.A.', 'c.a.', 'B.Com', 'B. Com',
    'M. Com', 'M.Com', 'M. Com .', 'ME', 'M.E', 'M.E.', 'MS', 'M.S', 'BTECH',
    'B.TECH', 'M.TECH', 'MTECH', 'PHD', 'phd', 'ph.d', 'Ph.D.', 'MBA', 'mba',
    'graduate', 'post-graduate', '5 year integrated masters', 'masters', 'SSC',
    'HSC', 'CBSE', 'ICSE', 'X', 'XII', 'Usha Mittal Institute of Technology',
    'Jawaharlal Nehru University', 'R.N.Podar'
]


def extract_education(resume_text):
    nlp_text = nlp(resume_text)
    # Sentence Tokenizer
    nlp_text = [sent.text.strip() for sent in nlp_text.sents]
    edu = {}
    # Extract education degree
    for index, text in enumerate(nlp_text):
        #print(index, text), print('-'*50)
        for tex in text.split():
            # Replace all special symbols
            tex = re.sub(r'[?|$|.|!|,]', r'', tex)
            print(tex)
            if tex.upper() in EDUCATION and tex not in STOPWORDS:
                edu[tex] = text + nlp_text[index + 1]
                print(edu.keys())
    return list(edu.values())

# noqa: T001
