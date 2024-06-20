---
title: Zeilenhöhe und Spaltenbreite in Python anpassen
type: docs
weight: 10
url: /de/java/adjusting-row-height-and-column-width-in-python/
keywords: Erstellen von XLSX in Python, Erstellen von XLS in Python, XLS Python, XLSX Python, Zeilenhöhe Python, Spaltenbreite Python, Excel Python
description: Verwenden Sie die Python Excel API, um Excel Dateien in Python zu erstellen. Passen Sie die Zeilenhöhe und Spaltenbreite in XLSX oder XLS in Ihren Python Anwendungen ohne MS Office an.
---

## **Excel-Tabellenkalkulationen in Python - Anpassen der Zeilenhöhe und Spaltenbreite**
### **Einstellen der Zeilenhöhe**
Mit Aspose.Cells ist es möglich, die Höhe einer einzelnen Zeile in Python durch Aufrufen der Methode setRowHeight der Cells-Sammlung festzulegen. Die Methode setRowHeight nimmt die folgenden Parameter an:

- **Zeilenindex**, der Index der Zeile, deren Höhe geändert wird.
- **Zeilenhöhe**, die auf die Zeile anzuwendende Zeilenhöhe.

**Python-Code**

{{< highlight python >}}

 def set_row_height(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Setting the height of the second row to 13

cells.setRowHeight(1, 13)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Set Row Height.xls")

print "Set Row Height Successfully." 

{{< /highlight >}}
### **Die Spaltenbreite festlegen**
Rufen Sie die Breite einer Spalte durch Aufrufen der Methode setColumnWidth der Sammlung Cells ein. Die Methode setColumnWidth nimmt die folgenden Parameter an:

- **Spaltenindex**, der Index der Spalte, deren Breite geändert wird.
- **Spaltenbreite**, die gewünschte Spaltenbreite.

**Python-Code**

{{< highlight python >}}

 def set_column_width(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Setting the width of the second column to 17.5

cells.setColumnWidth(1, 17.5)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Set Column Width.xls")

print "Set Column Width Successfully." 

{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie **Anpassung von Zeilenhöhe und Spaltenbreite (Aspose.Cells)** von einer der unten genannten Social-Coding-Websites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
