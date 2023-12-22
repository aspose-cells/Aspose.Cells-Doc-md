---
title: Adatta automaticamente righe e colonne in Python
type: docs
weight: 20
url: /it/java/autofit-rows-and-columns-in-python/
description: Scopri come adattare automaticamente righe e colonne tramite Aspose.Cells for Python tramite Java API.
keywords: How to Autofit Rows and Columns in Python Via Java, Autofit Rows Data in workbook using Python Via Java, Python Via Java Autofit Columns Data. 
---
##  **Come adattare automaticamente righe e colonne**
###  **Come adattare automaticamente la riga**
L'approccio più semplice per ridimensionare automaticamente la larghezza e l'altezza di una riga consiste nel chiamare il metodo autoFitRow della classe Worksheet. Il metodo autoFitRow accetta come parametro un indice di riga (della riga da ridimensionare).

**Python Cod**

{{< highlight "python" >}}

 def autofit_row(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Auto-fitting the 3rd row of the worksheet

worksheet.autoFitRow(2)

\# Auto-fitting the 3rd row of the worksheet based on the contents in a range of

\# cells (from 1st to 9th column) within the row

# worksheet.autoFitRow(2,0,8) # Uncomment this line if you to do AutoFit Row in a Range of Cells. Also, comment line 288.

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Autofit Row.xls")

print "Autofit Row Successfully." 

{{< /highlight >}}
###  **Come adattare automaticamente la colonna**
Il modo più semplice per ridimensionare automaticamente la larghezza e l'altezza di una colonna è chiamare il metodo autoFitColumn della classe Worksheet. Il metodo autoFitColumn prende come parametro l'indice della colonna (della colonna che sta per essere ridimensionata).

**Python Cod**

{{< highlight "python" >}}

 def autofit_column(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Auto-fitting the 4th column of the worksheet

worksheet.autoFitColumn(3)

\# Auto-fitting the 4th column of the worksheet based on the contents in a range of

\# cells (from 1st to 9th row) within the column

# worksheet.autoFitColumn(3,0,8) #Uncomment this line if you to do AutoFit Column in a Range of Cells. Also, comment line 310.

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Autofit Column.xls")

print "Autofit Column Successfully." 

{{< /highlight >}}
##  **Scarica il codice in esecuzione**
Scaricamento**Adatta automaticamente righe e colonne (Aspose.Cells)**da uno qualsiasi dei siti di social coding indicati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
