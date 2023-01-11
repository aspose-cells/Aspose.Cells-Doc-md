﻿---
title: Ausblenden und Anzeigen von Zeilen und Spalten in Python
type: docs
weight: 50
url: /de/java/hiding-and-showing-rows-and-columns-in-python/
---
## **Aspose.Cells – Steuern der Sichtbarkeit von Zeilen und Spalten**
### **Zeilen und Spalten ausblenden**
Entwickler können eine Zeile oder Spalte ausblenden, indem sie die Methoden HideRow und HideColumn der Sammlung Cells aufrufen. Beide Methoden verwenden den Zeilen-/Spaltenindex als Parameter, um die bestimmte Zeile oder Spalte auszublenden.

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
### **Zeilen und Spalten anzeigen**
Entwickler können jede ausgeblendete Zeile oder Spalte sichtbar machen, indem sie die Methoden UnhideRow und UnhideColumn der Sammlung Cells aufrufen. Beide Methoden nehmen zwei Parameter:

- **Rowor-Spaltenindex**- der Index einer Zeile oder Spalte, der verwendet wird, um die bestimmte Zeile oder Spalte anzuzeigen.
- **Zeilenhöhe oder Spaltenbreite**- die Zeilenhöhe oder Spaltenbreite, die der Zeile oder Spalte zugewiesen wird, nachdem sie angezeigt wurde.

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
## **Laufcode herunterladen**
 Download**Steuern der Sichtbarkeit von Zeilen und Spalten (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)