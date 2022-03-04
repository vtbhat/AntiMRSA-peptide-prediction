import re
import pandas as pd

file1= open("path/Downloads/Queryresults.txt", "r").readlines()
dictofmrsa = {}

for i in file1:
    APids = re.search("AP\d\d\d\d\d", i)#Find APD ID
    if APids != None:
        APidind = APids.group()#Add APD ID as a key in the dictionary
        dictofmrsa[APidind] = ""
    peptideseq = re.search("(?<=\t).+?(?=\s)", i)#Find correspoding amino acid sequence of the peptide
    if peptideseq != None:
        peptideseqind = peptideseq.group()
        dictofmrsa[APidind] = peptideseqind#Add the peptide sequence as a value in the dictionary

(pd.DataFrame.from_dict(data=dictofmrsa, orient='index').to_csv('C:/Users/VARSHA BHAT/Documents/MRSApeptides.csv', header=False))#Convert the dictionary to CSV
