---
title: Ein- und Ausblenden von Zeilen und Spalten in Python
type: docs
weight: 50
url: /de/java/hiding-and-showing-rows-and-columns-in-python/
description: Erfahren Sie, wie Sie Zeilen und Spalten über Aspose.Cells for Python über Java API ein- und ausblenden.
keywords: How to Hide and Show Rows and Columns in Python Via Java, Hide Rows and Columns using Python Via Java, Python Via Java Show Rows and Columns. 
---
##  **Aspose.Cells – Steuern der Sichtbarkeit von Zeilen und Spalten**
###  **So blenden Sie Zeilen und Spalten aus**
Entwickler können eine Zeile oder Spalte ausblenden, indem sie die Methoden HideRow bzw. HideColumn der Sammlung Cells aufrufen. Beide Methoden verwenden den Zeilen-/Spaltenindex als Parameter, um die spezifische Zeile oder Spalte auszublenden.

**Ruby-Code**

{{< highlight "ruby" >}}

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
###  **So zeigen Sie Zeilen und Spalten an**
Entwickler können jede ausgeblendete Zeile oder Spalte einblenden, indem sie die Methoden UnhideRow bzw. UnhideColumn der Sammlung Cells aufrufen. Beide Methoden benötigen zwei Parameter:

- **Zeilen- oder Spaltenindex**– der Index einer Zeile oder Spalte, der zur Anzeige der jeweiligen Zeile oder Spalte verwendet wird.
- **Zeilenhöhe oder Spaltenbreite**– die Zeilenhöhe oder Spaltenbreite, die der Zeile oder Spalte nach der Anzeige zugewiesen wird.

**Ruby-Code**

{{< highlight "ruby" >}}

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
##  **Laden Sie Running Code herunter**
 Herunterladen**Steuern der Sichtbarkeit von Zeilen und Spalten (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
