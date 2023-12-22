---
title: Autopassa rader och kolumner i Python
type: docs
weight: 20
url: /sv/java/autofit-rows-and-columns-in-python/
description: Lär dig hur du automatiskt anpassar rader och kolumner genom Aspose.Cells for Python Via Java API.
keywords: How to Autofit Rows and Columns in Python Via Java, Autofit Rows Data in workbook using Python Via Java, Python Via Java Autofit Columns Data. 
---
##  **Hur man automatiskt anpassar rader och kolumner**
###  **Hur man autopassar rad**
Det enklaste sättet att automatiskt anpassa bredd och höjd på en rad är att anropa Worksheet-klassens autoFitRow-metod. AutoFitRow-metoden tar ett radindex (för raden som ska ändras storlek) som en parameter.

**Python Kod**

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
###  **Hur man automatiskt anpassar kolumn**
Det enklaste sättet att automatiskt anpassa bredden och höjden på en kolumn är att anropa Worksheet-klassens autoFitColumn-metod. AutoFitColumn-metoden tar kolumnindex (för kolumnen som ska ändras storlek) som en parameter.

**Python Kod**

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
##  **Ladda ner Running Code**
Ladda ner**Autopassa rader och kolumner (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
