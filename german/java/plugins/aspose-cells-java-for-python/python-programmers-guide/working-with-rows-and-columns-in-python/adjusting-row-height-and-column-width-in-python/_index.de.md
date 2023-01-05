---
title: Anpassen der Zeilenhöhe und Spaltenbreite in Python
type: docs
weight: 10
url: /de/java/adjusting-row-height-and-column-width-in-python/
keywords: create XLSX in Python, create XLS in Python, XLS python, XLSX python, row height python, column width python, Excel pytho
description: Verwenden Sie Python Excel API, um Excel-Dateien in Python zu erstellen. Passen Sie Zeilenhöhe und Spaltenbreite in XLSX oder XLS in Ihren Python Anwendungen ohne MS Office an.
---
## **Excel-Tabellen in Python – Anpassen der Zeilenhöhe und Spaltenbreite**
### **Einstellen der Zeilenhöhe**
Mit Aspose.Cells ist es möglich, die Höhe einer einzelnen Zeile in Python festzulegen, indem die Methode setRowHeight der Sammlung Cells aufgerufen wird. Die setRowHeight-Methode übernimmt die folgenden Parameter:

- **Zeilenindex**, der Index der Zeile, deren Höhe Sie ändern.
- **Zeilenhöhe**, die Zeilenhöhe, die auf die Zeile angewendet werden soll.

**Python Code**

{{< highlight "python" >}}

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
### **Einstellen der Spaltenbreite**
Legen Sie die Breite einer Spalte fest, indem Sie die Methode setColumnWidth der Sammlung Cells aufrufen. Die setColumnWidth-Methode übernimmt die folgenden Parameter:

- **Spaltenindex**, der Index der Spalte, deren Breite Sie ändern.
- **Spaltenbreite**, die gewünschte Spaltenbreite.

**Python Code**

{{< highlight "python" >}}

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
## **Laufcode herunterladen**
Download**Zeilenhöhe und Spaltenbreite anpassen (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
