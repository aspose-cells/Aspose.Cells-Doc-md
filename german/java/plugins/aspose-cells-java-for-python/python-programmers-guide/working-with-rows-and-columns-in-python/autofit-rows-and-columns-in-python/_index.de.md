---
title: Zeilen und Spalten in Python anpassen
type: docs
weight: 20
url: /de/java/autofit-rows-and-columns-in-python/
description: Erfahren Sie, wie Sie Zeilen und Spalten über das Aspose.Cells für Python Via Java API automatisch anpassen.
keywords: Wie man Zeilen und Spalten in Python Via Java automatisch anpasst, Zeilendaten im Workbook mit Python Via Java anpasst, Python Via Java Spaltendaten automatisch anpasst. 
---

## **Wie man Zeilen und Spalten automatisch anpasst**
### **Wie man eine Zeile automatisch anpasst**
Der einfachste Ansatz zum automatischen Anpassen der Breite und Höhe einer Zeile besteht darin, die Methode autoFitRow der Klasse Worksheet aufzurufen. Die Methode autoFitRow nimmt einen Zeilenindex (der Zeile, die angepasst werden soll) als Parameter an.

**Python-Code**

{{< highlight python >}}

 def autofit_row(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Auto-fitting the 3rd row of the worksheet

worksheet.autoFitRow(2)

\# Auto-fitting the 3rd row of the worksheet based on the contents in a range of

\# cells (from 1st to 9th column) within the row

#worksheet.autoFitRow(2,0,8) # Uncomment this line if you to do AutoFit Row in a Range of Cells. Also, comment line 288.

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Autofit Row.xls")

print "Autofit Row Successfully." 

{{< /highlight >}}
### **Wie man eine Spalte automatisch anpasst**
Der einfachste Weg, die Breite und Höhe einer Spalte automatisch anzupassen, besteht darin, die Methode autoFitColumn der Klasse Worksheet aufzurufen. Die Methode autoFitColumn erhält den Spaltenindex (der Spalte, die gerade angepasst wird) als Parameter.

**Python-Code**

{{< highlight python >}}

 def autofit_column(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Auto-fitting the 4th column of the worksheet

worksheet.autoFitColumn(3)

\# Auto-fitting the 4th column of the worksheet based on the contents in a range of

\# cells (from 1st to 9th row) within the column

#worksheet.autoFitColumn(3,0,8) #Uncomment this line if you to do AutoFit Column in a Range of Cells. Also, comment line 310.

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Autofit Column.xls")

print "Autofit Column Successfully." 

{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie **Autofit Rows and Columns (Aspose.Cells)** von einer der unten genannten sozialen Plattformen herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
