# Analyse-sentiment-using-scrap-data

# OBJECTIVE
The objective of this assignment is to extract textual data articles from the given URL and perform text analysis to compute variables that are explained below. 

# Task
1	Sentimental Analysis	

1.1	Cleaning using Stop Words Lists	

1.2	Creating dictionary of Positive and Negative words

1.3	Extracting Derived variables	

2	Analysis of Readability

3	Average Number of Words Per Sentence

4	Complex Word Count

5	Word Count

6	Syllable Count Per word

7	Personal Pronouns

8	Average Word Length	

#	Data Extraction
For each of the articles, given in the input.xlsx file, extract the article text using python Scrapy and save the extracted article in a text file with URL_ID as its file name.
While extracting text, program extracts only the article title and the article text. It should not extract the website header, footer, or anything other than the article text. 

# Data Analysis
For each of the extracted texts from the article, perform textual analysis and compute variables, given in the output structure excel file. You need to save the output in the exact order as given in the output structure file, “Output Data Structure.xlsx”


# Step After scrap data from website
1	Sentimental Analysis
Sentimental analysis is the process of determining whether a piece of writing is positive, negative or neutral. The below Algorithm is designed for use on Financial Texts. It consists of steps:
1.1	Cleaning using Stop Words Lists
The Stop Words Lists (found here) are used to clean the text so that Sentiment Analysis can be performed by excluding the words found in Stop Words List.
1.2	Creating dictionary of Positive and Negative words
The Master Dictionary (found here) is used for creating a dictionary of Positive and Negative words. We add only those words in the dictionary if they are not found in the Stop Words Lists. Use this url if above does not work https://sraf.nd.edu/textual-analysis/resources/ 
1.3	Extracting Derived variables
We convert the text into a list of tokens using the nltk tokenize module and use these tokens to calculate the 4 variables described below:
Positive Score: This score is calculated by assigning the value of +1 for each word if found in the Positive Dictionary and then adding up all the values.
Negative Score: This score is calculated by assigning the value of -1 for each word if found in the Negative Dictionary and then adding up all the values. We multiply the score with -1 so that the score is a positive number.
Polarity Score: This is the score that determines if a given text is positive or negative in nature. It is calculated by using the formula: 
Polarity Score = (Positive Score – Negative Score)/ ((Positive Score + Negative Score) + 0.000001)
Range is from -1 to +1
Subjectivity Score: This is the score that determines if a given text is objective or subjective. It is calculated by using the formula: 
Subjectivity Score = (Positive Score + Negative Score)/ ((Total Words after cleaning) + 0.000001)
Range is from 0 to +1

2	Analysis of Readability
Analysis of Readability is calculated using the Gunning Fox index formula described below.
Average Sentence Length = the number of words / the number of sentences
Percentage of Complex words = the number of complex words / the number of words 
Fog Index = 0.4 * (Average Sentence Length + Percentage of Complex words)

3	Average Number of Words Per Sentence
The formula for calculating is:
Average Number of Words Per Sentence = the total number of words / the total number of sentences

4	Complex Word Count
Complex words are words in the text that contain more than two syllables.

5	Word Count
We count the total cleaned words present in the text by 
1.	removing the stop words (using stopwords class of nltk package).
2.	removing any punctuations like ? ! , . from the word before counting.

6	Syllable Count Per Word
We count the number of Syllables in each word of the text by counting the vowels present in each word. We also handle some exceptions like words ending with "es","ed" by not counting them as a syllable.

7	Personal Pronouns
To calculate Personal Pronouns mentioned in the text, we use regex to find the counts of the words - “I,” “we,” “my,” “ours,” and “us”. Special care is taken so that the country name US is not included in the list.

8	Average Word Length
Average Word Length is calculated by the formula:
Sum of the total number of characters in each word/Total number of words

# Technology
Python,Scrapy,pandas,nltk(Natural Language Toolkit).
