CSC1034: Practical 2
====================

This package allows analysis and display of proteins from Uniprot.

Usage
====================
pipenv run python uniplot.py [--depth depth] [--directory "/example/directory"] dump/list/average/small/plot/plotpie


Command Line Arguments
====================
**--directory**

allows the user to pass in the path to a custom uniplot file

**--depth**

allows the user to specify how many taxa down to go

**dump**

prints all information about every protein

**list**

prints the names of every protein

**average**

prints the average length of every protein

**small**

prints the average length of every protein in the smaller uniprot file

**plot**

plots a graph of frequency against taxa for every protein

**plotpie**

plots a pie chart showing the proportion of different taxa
