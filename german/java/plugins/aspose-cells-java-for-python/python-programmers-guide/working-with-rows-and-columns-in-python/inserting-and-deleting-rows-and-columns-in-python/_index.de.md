---
title: Einfügen und Löschen von Zeilen und Spalten in Python
type: docs
weight: 60
url: /de/java/inserting-and-deleting-rows-and-columns-in-python/
keywords: "Erstellen Sie XLSX in Python, erstellen Sie XLS in Python, XLS Python, XLSX Python, XLT Python, XLTX Python, Zeile einfügen Python, Spalte einfügen Python, Excel Python"
description: Verwenden Sie Python Excel API, um Excel Tabellen in Python zu erstellen. Fügen Sie in Ihren Python Anwendungen Zeilen von XLSX oder XLS ein oder löschen Sie diese, ohne MS Office.
---

## **Erstellen von Excel-Tabellen in Python - Verwalten von Zeilen/Spalten**
### **Einlegen einer Zeile**
Fügen Sie eine Zeile an einer beliebigen Stelle ein, indem Sie die Methode insertRows der Cells-Sammlung aufrufen. Die Methode insertRows nimmt den Index der Zeile, an der die neue Zeile eingefügt wird, als ersten Argument und die Anzahl der einzufügenden Zeilen als zweites Argument. Folgende Schritte sind zu befolgen:

- XLS- oder XLSX-Arbeitsmappe laden
- Arbeitsblatt aufrufen
- Die Zeile einfügen
- Als XLS- oder XLSX-Arbeitsmappe speichern

**Python-Code**

{{< highlight python >}}

 def insert_row(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + "Book1.xls")

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Inserting a row into the worksheet at 3rd position

worksheet.getCells().insertRows(2,1)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Insert Row.xls")

print "Insert Row Successfully." 

{{< /highlight >}}
### **Einfügen mehrerer Zeilen**
Um mehrere Zeilen in das Arbeitsblatt einzufügen, rufen Sie die Methode insertRows der Cells-Sammlung auf. Die Methode insertRows nimmt zwei Parameter:

- Zeilenindex, der Index der Zeile, ab der die neuen Zeilen eingefügt werden.
- Anzahl der Zeilen, Gesamtanzahl der Zeilen, die eingefügt werden müssen.

**Python-Code**

{{< highlight python >}}

 def insert_multiple_rows(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Inserting a row into the worksheet at 3rd position

worksheet.getCells().insertRows(2,10)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Insert Multiple Rows.xls")

print "Insert Multiple Rows Successfully." 


{{< /highlight >}}
### **Löschen einer Zeile**
Um eine Zeile an einer beliebigen Stelle zu löschen, rufen Sie die Methode deleteRows der Cells Sammlung auf. Die deleteRows Methode nimmt zwei Parameter:

- Zeilenindex, der Index der Zeile, ab der die Zeilen gelöscht werden.
- Anzahl der Zeilen, Gesamtanzahl der Zeilen, die gelöscht werden müssen.

**Python-Code**

{{< highlight python >}}

 def delete_row(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Deleting 3rd row from the worksheet

worksheet.getCells().deleteRows(2,1,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Delete Row.xls")

print "Delete Row Successfully." 

{{< /highlight >}}
### **Mehrere Zeilen löschen**
Um mehrere Zeilen aus einem Arbeitsblatt zu löschen, rufen Sie die Methode deleteRows der Cells Sammlung auf. Die deleteRows Methode nimmt zwei Parameter:

- Zeilenindex, der Index der Zeile, ab der die Zeilen gelöscht werden.
- Anzahl der Zeilen, Gesamtanzahl der Zeilen, die gelöscht werden müssen.

**Python-Code**

{{< highlight python >}}

 def delete_multiple_rows(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Deleting 10 rows from the worksheet starting from 3rd row

worksheet.getCells().deleteRows(2,10,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Delete Multiple Rows.xls")

print "Delete Multiple Rows Successfully." 


{{< /highlight >}}
### **Einfügen einer Spalte**
Entwickler können auch eine Spalte in das Arbeitsblatt an einer beliebigen Stelle einfügen, indem sie die insertColumns Methode der Cells Sammlung aufrufen. Die insertColumns Methode nimmt zwei Parameter:

- Spaltenindex, der Index der Spalte, von der die Spalte eingefügt werden soll.
- Anzahl der Spalten, Gesamtanzahl der Spalten, die eingefügt werden müssen.

**Python-Code**

{{< highlight python >}}

 def insert_column(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Inserting a column into the worksheet at 2nd position

worksheet.getCells().insertColumns(1,1)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Insert Column.xls")

print "Insert Column Successfully." 


{{< /highlight >}}
### **Löschen einer Spalte**
Um eine Spalte aus dem Arbeitsblatt an einer beliebigen Stelle zu löschen, rufen Sie die Methode deleteColumns der Cells Sammlung auf. Die deleteColumns Methode nimmt die folgenden Parameter:

- Spaltenindex, der Index der Spalte, von der die Spalte gelöscht werden soll.
- Anzahl der Spalten, Gesamtanzahl der Spalten, die gelöscht werden müssen.
- Zellen verschieben, Boolescher Parameter, um anzuzeigen, ob die Zellen nach dem Löschen nach links verschoben werden sollen.

**Python-Code**

{{< highlight python >}}

 def delete_column(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Deleting a column from the worksheet at 2nd position

worksheet.getCells().deleteColumns(1,1,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Delete Column.xls")

print "Delete Column Successfully." 


{{< /highlight >}}
## **Laufenden Code herunterladen**
**Zeilen/Spalten verwalten (Aspose.Cells)** von einer der unten genannten Social-Coding-Websites herunterladen:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
