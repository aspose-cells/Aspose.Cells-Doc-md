---
title: Gruppierung und Entgruppierung von Zeilen und Spalten in Python
type: docs
weight: 40
url: /de/java/grouping-and-ungrouping-rows-and-columns-in-python/
description: Erfahren Sie, wie Sie Zeilen und Spalten durch das Aspose.Cells for Python Via Java API gruppieren und entgruppieren.
keywords: Wie man Zeilen und Spalten in Python Via Java gruppieren und entgruppieren kann, Gruppieren von Zeilen und Spalten mit Python Via Java, Entgruppieren von Zeilen und Spalten mit Python Via Java. 
---

## **Gruppierungs- und Entgruppierungsverwaltung von Zeilen & Spalten in Aspose.Cells für Python via Java**
### **Wie man Zeilen & Spalten in Python gruppiert**
Es ist möglich, Zeilen oder Spalten zu gruppieren, indem die Methoden groupRows und groupColumns der Cells-Sammlung aufgerufen werden. Beide Methoden akzeptieren die folgenden Parameter:

- Erster Zeilen-/Spaltenindex, die erste Zeile oder Spalte in der Gruppe.
- Letzter Zeilen-/Spaltenindex, die letzte Zeile oder Spalte in der Gruppe.
- Ist versteckt, ein boolescher Parameter, der angibt, ob Zeilen/Spalten nach dem Gruppieren ausgeblendet werden sollen oder nicht.

**Python-Code**

{{< highlight python >}}

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
### **Wie man Zeilen & Spalten mit Python entgruppiert**
Gruppierte Zeilen oder Spalten aufheben, indem die Methoden UngroupRows und UngroupColumns der Cells-Sammlung aufgerufen werden. Beide Methoden akzeptieren die gleichen Parameter:

- Erster Zeilen- oder Spaltenindex, die erste Zeile/Spalte, die aufgehoben werden soll.
- Letzter Zeilen- oder Spaltenindex, die letzte Zeile/Spalte, die aufgehoben werden soll.

**Python-Code**

{{< highlight python >}}

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
## **Laufenden Code herunterladen**
Gruppierung & Aufhebung der Gruppierung von Zeilen & Spalten (Aspose.Cells) von einer der unten genannten sozialen Codierungsseiten herunterladen:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
