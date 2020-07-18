# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 00:58:52 2020

@author: Swapnil Sharma

URL : https://www.geeksforgeeks.org/python-lemmatization-with-nltk/
"""

# import these modules 
from nltk.stem import WordNetLemmatizer 
  
lemmatizer = WordNetLemmatizer() 
  
print("rocks :", lemmatizer.lemmatize("rocks")) 
print("corpora :", lemmatizer.lemmatize("corpora")) 
  
# a denotes adjective in "pos" 
print("better :", lemmatizer.lemmatize("better", pos ="a")) 

print("rocks :", lemmatizer.lemmatize("worse", pos ="a")) 


print("better :", lemmatizer.lemmatize("better") )

print("better :", lemmatizer.lemmatize("worse") )


