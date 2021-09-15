# AntiMRSA-peptide-prediction
This repository consists of scripts to create a database of antimicrobial peptides exhibiting anti-MRSA (methicillin-resistant Staphylococcus aureus) activity from publicly available online databases, and to create a machine learning-based classifier to predict peptides as anti-MRSA

## AntiMRSApeptideparser.py
Antimicrobial Peptide Database (APD) is a publicly available database of antimicrobial peptides. Each peptide has an identifier of the format 'AP(5 digits)'. The database can be queried to obtain a list of peptides exhibiting specific activity

Input: Input file containing the text from a search query on APD (here, anti-MRSA)

Output: CSV file containing the APD ID and the correspoding amino acid sequence of the peptide
