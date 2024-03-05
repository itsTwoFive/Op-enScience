# Alvaro Gonzalez Mendez's Open Science Project
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10782920.svg)](https://doi.org/10.5281/zenodo.10782920)
## Description
Individual practice for the course Open Science and Artificial Intelligence at UPM.
### The scripts
This repository contains 3 Scripts that using already analyzed pdf with grobid will do the next tasks:
1. Draw a keyword cloud based on the abstract information
2. Create a visualization showing the number of figures per article.
3. Create a list of the links (references)* found in each paper.

*In order to proceed with the exercise I changed the expected behivor of the 3rd script becouse I couldn't find the way to fetch thelinks from the grobisd output files, so now it Lists all the references and it's authors in a txt document.
## Requirements
In orther to run the script your machine should count with the following dependencies:
- Grobid server 0.8.1-SNAPSHOT*
- Python 3.12 or above
- matplotlib 3.8.3
- grobid-client 0.8.5*
- wordcloud 1.9.3
- requests 2.31.0

*Only if you want to procces pdfs, if you already have the files processed into grobid.tei.xml files don't need these
## Instalation Instructions
In order to run the program you should follow the next instructions.
1. Set up a new Python 3.12 enviroment
2. Install the needed libraries
```
pip install matplotlib==3.8.3
pip install wordcloud==1.9.3
pip install requests==2.31.0
```
3. Clone the repository and change the current directory to the code's path.
```
git clone https://github.com/itsTwoFive/Op-enScience
cd Op-enScience
```
4. Install docker if you haven't and then run the grobid server. More info in [Grobid](https://github.com/kermitt2/grobid) 
```
docker run --rm --init --ulimit core=0 -p 8070:8070 grobid/grobid:0.8.1-SNAPSHOT
```
5. Download python grobid client. More info in [Grobid Client](https://github.com/kermitt2/grobid_client_python)
```
git clone https://github.com/kermitt2/grobid_client_python
```
6. Now you can run the analyzer and later any of the 3 scripts. (In order to analyze any pdf you must copy them into *pdf* dir)
```
python analyzePapers.py
python 1_kewordcloud.py
python 2_number_o_figures.py
python 3_references.py
```
## Execution Instructions
In order to execute the scripts you will to preprocess the wanted pdfs using grobid. This can be done by copying the pdf files into the dir "pdf" and executing the python script *analyzePapers.py*.
Then once you have preprocessed the papers, you can make use of the three following scripts orderless.
- 1_kewordcloud.py
- 2_number_o_figures.py
- 3_references.py
## Running examples
Each one of the scripts has its unique output, depending wich one is executed you will get different solutions in different ways. The repository contaisn 11 papers to test in the dir *pdfs*, you can add as much as you want here as it would act as the input directory.
### 1_kewordcloud.py
This script will create a 1920x1080 image with the keywords used in the analyzed pdfs.
![WordCloud](https://github.com/itsTwoFive/Op-enScience/blob/main/wordcloud.png)
### 2_number_o_figures.py
This script will show on commandline a table counting the number of figures per document. Similar to:
```
-------------------------------------------------------
00726791.pdf                                  ==> 38
14496638977 abstract.pdf                      ==> 0
45b915890c92195523c0bc867d5b3d4e9232.pdf      ==> 5
HADS.pdf                                      ==> 2
livak-2001.pdf                                ==> 3
MathBohem_120-1995-3_8.pdf                    ==> 2
nsga2-ieee-trans-ec-2002.pdf                  ==> 28
random_forest.pdf                             ==> 13
TamuraStecher13a.pdf                          ==> 3
thematic_analysis_revised_-_final.pdf         ==> 6
wang03-reprint.pdf                            ==> 10
-------------------------------------------------------
Total number of figures                       ==> 110
```
### 3_references.py
This script will create a .txt file showing all the references in the text. Similar to:

```
----------------------------------------------------------------------------------------------------

Fichero MathBohem_120-1995-3_8.pdf:

	Jabalpur R K Sara, S S Thaku, a-COMPACT FUZZY TOPOLOGICAL SPACE.
	C L Chan, Fuzzy topological space.
	O Njdste, On some classes of nearly open set.
	S S Thaku, S N Maheshwar, On a-irresolute mappin.
	S S Thaku, S N Maheshwar, On a-continuous mappin.
	S S Thaku, S N Maheshwar, On a-compact space.
	S , I A Hassania, A S Mashhou, El-deeb: a-continuous and a-open mapping.
	L A Zade, Fuzzy set.

----------------------------------------------------------------------------------------------------
```

## Prefered Citation
The main and only author of this code is Alvaro Gonzalez Mendez, student at Universidad Politecnica de Madrid, ETSIINF
## Where to get help
If help needed, you can contact me at alvaro.gmendez@alumnos.upm.es
