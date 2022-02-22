# -*- coding: utf-8 -*-
from fileinput import filename
import os
import re

file_name="motyw_tygodniowy"+"/"+"fārsī.csv"
with open(file_name, 'r', encoding="utf-8") as file_csv:
    text=file_csv.read()
file_csv.close

wzor1 = r'\[[0-9][0-9]:[0-9][0-9]\] '
wzor2 = r'Kucyk: '
text=re.sub(wzor2, '', text)
text=re.sub(wzor1, '', text)
print(text)
print(type(text))
with open(file_name, 'w', encoding="utf-8") as file_csv:
    file_csv.write(str(text))
file_csv.close()