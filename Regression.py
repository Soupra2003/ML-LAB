import re
text = """My name is Souvik Pramanik.
             I am from Panskura, East Medinipur, WestBangal, India.
             My mail is souvik@gmail.com or soupra@gmail.com.
             My phone Number is +919609995868
             I completed my 10+2 studies from Deriachak Sri Aurobindo Vidyamath.
             Now I am Pursuing B.tech in CSE at Adamas University.
             """
pattern1 = "Souvik Pramanik"
match = re.search(pattern1, text)
if match:
    print("Match found:", match.group())
else:
    print("Match not found")    

pattern2 = "\d+"
match = re.findall(pattern2, text)  
if match:
    print("Match found:", match)
else:
    print("Match not found")    

pattern3 = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
match = re.findall(pattern3, text)
if match:
    print("Match found :", match)
else:
    print("Match Not found")

patten4 = r"\+?\d{1,3}[-.\s]?\d{10}"
match = re.findall(patten4, text)           
if match:
    print("Match found :", match)
else:
    print("Match Not found")

from spellchecker import SpellChecker
spell = SpellChecker()
def is_spelled_correctly(line):
    correctedline = []
    for word in line:
        correctedline.append(spell.correction(word))
    return (line == correctedline)

sample_list = text.split()
print("Sample List:", sample_list)
print(is_spelled_correctly(sample_list))

import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
for token in doc.ents:
    if token.label_ == "PERSON":
       print(token.text, token.label_)
    elif token.label_ == "GPE":
        print(token.text, token.label_)
    