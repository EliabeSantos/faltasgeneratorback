import pandas as pd
titanic = pd.read_excel("manha.xls", header=[0], nrows=1000)
serie = ''
index = 0
for row in titanic.itertuples():
    if(type(row[6]) == str and "Seriação" in row[6]):
        if(serie == row[6] + " " + row[14]):
            index = index + 1
        serie = row[6] + " " + row[14]
    if row[13] == 'Matriculado':
         print(f" Col1: { row[3], row[5], row[13], serie}")