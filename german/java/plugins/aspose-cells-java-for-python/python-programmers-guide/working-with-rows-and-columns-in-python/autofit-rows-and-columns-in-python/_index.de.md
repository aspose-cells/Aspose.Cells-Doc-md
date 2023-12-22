---
title: Zeilen und Spalten automatisch anpassen in Python
type: docs
weight: 20
url: /de/java/autofit-rows-and-columns-in-python/
description: Erfahren Sie, wie Sie Zeilen und Spalten über Aspose.Cells for Python Via Java API automatisch anpassen.
keywords: How to Autofit Rows and Columns in Python Via Java, Autofit Rows Data in workbook using Python Via Java, Python Via Java Autofit Columns Data. 
---
##  **So passen Sie Zeilen und Spalten automatisch an**
###  **So passen Sie eine Zeile automatisch an**
Der einfachste Ansatz zum automatischen Anpassen der Breite und Höhe einer Zeile besteht darin, die autoFitRow-Methode der Worksheet-Klasse aufzurufen. Die autoFitRow-Methode verwendet einen Zeilenindex (der Zeile, deren Größe geändert werden soll) als Parameter.

**Python Code**

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
###  **So passen Sie eine Spalte automatisch an**
Der einfachste Weg, die Breite und Höhe einer Spalte automatisch anzupassen, besteht darin, die Methode autoFitColumn der Worksheet-Klasse aufzurufen. Die autoFitColumn-Methode verwendet den Spaltenindex (der Spalte, deren Größe geändert werden soll) als Parameter.

**Python Code**

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
##  **Laden Sie Running Code herunter**
Herunterladen**Zeilen und Spalten automatisch anpassen (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
