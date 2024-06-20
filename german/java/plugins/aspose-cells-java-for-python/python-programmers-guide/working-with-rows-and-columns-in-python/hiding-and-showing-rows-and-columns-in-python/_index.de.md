---
title: Zeilen und Spalten in Python ausblenden und anzeigen
type: docs
weight: 50
url: /de/java/hiding-and-showing-rows-and-columns-in-python/
description: Lernen Sie, wie Sie Zeilen und Spalten mit der Aspose.Cells for Python Via Java API ausblenden und anzeigen.
keywords: Ausblenden und Anzeigen von Zeilen und Spalten in Python Via Java, Ausblenden von Zeilen und Spalten mit Python Via Java, Zeilen und Spalten anzeigen mit Python Via Java. 
---

## **Aspose.Cells - Steuerung der Sichtbarkeit von Zeilen & Spalten**
### **Wie man Zeilen und Spalten ausblendet**
Entwickler können eine Zeile oder Spalte verbergen, indem sie die Methoden HideRow und HideColumn der Cells-Sammlung aufrufen. Beide Methoden nehmen den Zeilen-/Spaltenindex als Parameter, um die spezifische Zeile oder Spalte zu verbergen.

**Ruby-Code**

{{< highlight ruby >}}

 def hide_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Hiding the 3rd row of the worksheet

cells.hideRow(2)

\# Hiding the 2nd column of the worksheet

cells.hideColumn(1)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Hide Rows And Columns.xls")

print "Hide Rows And Columns Successfully." 

{{< /highlight >}}
### **Wie man Zeilen und Spalten anzeigt**
Entwickler können eine versteckte Zeile oder Spalte wieder anzeigen, indem sie die Methoden UnhideRow und UnhideColumn der Cells-Sammlung aufrufen. Beide Methoden nehmen zwei Parameter:

- **Zeilen- oder Spaltenindex** - der Index einer Zeile oder Spalte, der verwendet wird, um die spezifische Zeile oder Spalte anzuzeigen.
- **Zeilenhöhe oder Spaltenbreite** - die Zeilenhöhe oder Spaltenbreite, die der Zeile oder Spalte nach dem Anzeigen zugewiesen wird.

**Ruby-Code**

{{< highlight ruby >}}

 def unhide_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Unhiding the 3rd row and setting its height to 13.5

cells.unhideRow(2,13.5)

\# Unhiding the 2nd column and setting its width to 8.5

cells.unhideColumn(1,8.5)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Unhide Rows And Columns.xls")

print "Unhide Rows And Columns Successfully." 

{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie die Steuerung der Sichtbarkeit von Zeilen & Spalten (Aspose.Cells) von einer der unten genannten Social-Coding-Sites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
