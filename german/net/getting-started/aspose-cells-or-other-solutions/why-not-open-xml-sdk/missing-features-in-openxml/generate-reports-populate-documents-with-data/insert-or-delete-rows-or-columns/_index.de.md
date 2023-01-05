---
title: Zeilen oder Spalten einfügen oder löschen
type: docs
weight: 20
url: /de/net/insert-or-delete-rows-or-columns/
---
Unabhängig davon, ob wir ein neues Arbeitsblatt von Grund auf neu erstellen oder an einem vorhandenen Arbeitsblatt arbeiten, müssen wir möglicherweise zusätzliche Zeilen oder Spalten in das Arbeitsblatt einfügen, um mehr Daten aufzunehmen oder aus anderen Gründen. Umgekehrt kann es auch erforderlich sein, Zeilen oder Spalten von bestimmten Positionen des Arbeitsblatts zu löschen.
## **Zeilen/Spalten verwalten**
**Aspose.Cells** stellt eine Klasse Workbook bereit, die eine Excel-Datei darstellt. Die Workbook-Klasse enthält eine Worksheets-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Worksheet-Klasse dargestellt. Die Worksheet-Klasse stellt eine Cells-Sammlung bereit, die alle Zellen im Arbeitsblatt darstellt.

**Cells**collection bietet mehrere Methoden zum Verwalten von Zeilen oder Spalten in einem Arbeitsblatt, einige davon werden im Folgenden ausführlicher besprochen.
## **Einfügen einer Zeile**
 Entwickler können an beliebiger Stelle eine Zeile in das Arbeitsblatt einfügen, indem sie die Methode InsertRow der Sammlung Cells aufrufen.**Zeile einfügen** -Methode nimmt den Index der Zeile, in der die neue Zeile eingefügt wird.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Inserting a row into the worksheet at 3rd position

worksheet.Cells.InsertRow(2);

//Saving the modified Excel file

workbook.Save(MyDir + "Inserting Row.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Mehrere Zeilen einfügen**
Manchmal müssen Entwickler möglicherweise mehrere Zeilen in das Arbeitsblatt einfügen. Dies kann durch Aufrufen der InsertRows-Methode der Cells-Sammlung erfolgen. Die InsertRows-Methode benötigt zwei Parameter:

- **Zeilenindex**, der Index der Zeile, ab der die neuen Zeilen eingefügt werden
- **Anzahl der Reihen**, Gesamtzahl der Zeilen, die eingefügt werden müssen

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Inserting 10 rows into the worksheet starting from 3rd row

worksheet.Cells.InsertRows(2, 10);

//Saving the modified Excel file

workbook.Save(MyDir + "Inserting Mutiple Rows.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Löschen einer Zeile**
 Entwickler können an jeder Stelle eine Zeile aus dem Arbeitsblatt löschen, indem sie die aufrufen**Zeile löschen** Methode der Sammlung Cells.**Zeile löschen** -Methode nimmt den Index der Zeile, die gelöscht werden muss.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Deleting 3rd row from the worksheet

worksheet.Cells.DeleteRow(2);

//Saving the modified Excel file

workbook.Save(MyDir + "Deleting Rows.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Löschen mehrerer Zeilen**
Wenn Entwickler mehrere Zeilen aus dem Arbeitsblatt löschen müssen, kann dies auch durch Aufrufen der DeleteRows-Methode der Cells-Sammlung erfolgen. Die DeleteRows-Methode benötigt zwei Parameter:

- **Zeilenindex**, der Index der Zeile, aus der die Zeilen gelöscht werden.
- **Anzahl der Reihen**, Gesamtzahl der Zeilen, die gelöscht werden müssen.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Deleting 10 rows from the worksheet starting from 3rd row

worksheet.Cells.DeleteRows(2, 10);

//Saving the modified Excel file

workbook.Save(MyDir + "Deleting Mutiple Rows.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Einfügen einer Spalte**
Entwickler können auch an beliebiger Stelle eine Spalte in das Arbeitsblatt einfügen, indem sie die Methode InsertColumn der Sammlung Cells aufrufen. Die InsertColumn-Methode übernimmt den Index der Spalte, in die die neue Spalte eingefügt wird.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Inserting a column into the worksheet at 2nd position

worksheet.Cells.InsertColumn(1);

//Saving the modified Excel file

workbook.Save(MyDir + "Inserting Column.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Löschen einer Spalte**
Um eine Spalte an einer beliebigen Stelle aus dem Arbeitsblatt zu löschen, können Entwickler die Methode DeleteColumn der Sammlung Cells aufrufen. Die DeleteColumn-Methode übernimmt den Index der zu löschenden Spalte.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Deleting a column from the worksheet at 2nd position

worksheet.Cells.DeleteColumn(1);

//Saving the modified Excel file

workbook.Save(MyDir + "Deleting Column.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bit Bucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Work%20with%20Rows%20n%20Columns%20%28Aspose.Cells%29.zip)
