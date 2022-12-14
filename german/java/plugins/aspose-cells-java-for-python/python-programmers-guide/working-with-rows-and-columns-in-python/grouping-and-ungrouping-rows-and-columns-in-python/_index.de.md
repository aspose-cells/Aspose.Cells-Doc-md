---
title: Gruppieren und Aufheben der Gruppierung von Zeilen und Spalten in Python
type: docs
weight: 40
url: /de/java/grouping-and-ungrouping-rows-and-columns-in-python/
---
## **Aspose.Cells - Gruppenverwaltung von Zeilen und Spalten**
### **Gruppieren von Zeilen und Spalten**
Es ist möglich, Zeilen oder Spalten zu gruppieren, indem die Methoden groupRows und groupColumns der Sammlung Cells aufgerufen werden. Beide Methoden nehmen die folgenden Parameter:

- Index der ersten Zeile/Spalte, die erste Zeile oder Spalte in der Gruppe.
- Letzter Zeilen-/Spaltenindex, die letzte Zeile oder Spalte in der Gruppe.
- Ist ausgeblendet, ein boolescher Parameter, der angibt, ob Zeilen/Spalten nach der Gruppierung ausgeblendet werden sollen oder nicht.

**Python Code**

{{< highlight "python" >}}

 def group_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Grouping first six rows (from 0 to 5) and making them hidden by passing true

cells.groupRows(0,5,True)

\# Grouping first three columns (from 0 to 2) and making them hidden by passing true

cells.groupColumns(0,2,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Group Rows And Columns.xls")

print "Group Rows And Columns Successfully." 

{{< /highlight >}}
### **Gruppierung von Zeilen und Spalten aufheben**
Heben Sie die Gruppierung gruppierter Zeilen oder Spalten auf, indem Sie die Methoden UngroupRows und UngroupColumns der Sammlung Cells aufrufen. Beide Methoden verwenden die gleichen Parameter:

- Index der ersten Zeile oder Spalte, die erste Zeile/Spalte, deren Gruppierung aufgehoben werden soll.
- Letzter Zeilen- oder Spaltenindex, die letzte Zeile/Spalte, deren Gruppierung aufgehoben werden soll.

**Python Code**

{{< highlight "python" >}}

 def ungroup_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Group Rows And Columns.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Ungrouping first six rows (from 0 to 5)

cells.ungroupRows(0,5)

\# Ungrouping first three columns (from 0 to 2)

cells.ungroupColumns(0,2)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Ungroup Rows And Columns.xls")

print "Ungroup Rows And Columns Successfully." 

{{< /highlight >}}
## **Laufcode herunterladen**
 Download**Zeilen und Spalten gruppieren und Gruppierung aufheben (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
