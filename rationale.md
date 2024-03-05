
# Rationale
In order to prove my solutions, I checked each one of the scripts in the following manner.

## 1_keywordcloud.py
To verify this script, I ran it and checked if the words in the generated picture are the same as the keywords in the PDF papers I provided as input. In my own test case, I used papers related to neural networks, and the result satisfyingly displayed the keywords.

## 2_number_of_figures.py
To verify this script, I ran it and checked if the number of figures per paper is accurate, and it seems to be so.

## 3_references.py
This assessment was rather challenging, as I couldn't retrieve any link information for any paper using Grobid. Therefore, I modified its expected behavior to search for all references and their authors. It also functions effectively.
