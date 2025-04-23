---
title: Zeilen oder Spalten einfügen oder löschen
type: docs
weight: 20
url: /de/net/insert-or-delete-rows-or-columns/
---

Ob wir ein neues Arbeitsblatt von Grund auf erstellen oder an einem vorhandenen Arbeitsblatt arbeiten, möglicherweise müssen wir zusätzliche Zeilen oder Spalten in das Arbeitsblatt einfügen, um mehr Daten unterzubringen oder aus einem anderen Grund. Umgekehrt kann es auch erforderlich sein, Zeilen oder Spalten aus spezifischen Positionen des Arbeitsblatts zu löschen.
## **Verwalten von Zeilen/Spalten**
**Aspose.Cells** bietet eine Klasse, Workbook, die eine Excel-Datei repräsentiert. Die Workbook-Klasse enthält eine Worksheets-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Worksheet-Klasse repräsentiert. Die Worksheet-Klasse bietet eine Cells-Sammlung, die alle Zellen im Arbeitsblatt darstellt.

Die **Cells**-Sammlung bietet mehrere Methoden zum Verwalten von Zeilen oder Spalten in einem Arbeitsblatt, einige davon werden unten im Detail diskutiert.
## **Einlegen einer Zeile**
Entwickler können eine Zeile in das Arbeitsblatt an beliebiger Stelle einfügen, indem sie die Methode InsertRow der Cells-Sammlung aufrufen. Die **InsertRow**-Methode nimmt den Index der Zeile an, an der die neue Zeile eingefügt wird.

{{< highlight csharp >}}

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
## **Einfügen mehrerer Zeilen**
Manchmal müssen Entwickler möglicherweise mehrere Zeilen in das Arbeitsblatt einfügen. Dies kann durch Aufrufen der Methode InsertRows der Cells-Sammlung erfolgen. Die InsertRows-Methode nimmt zwei Parameter an:

- **Zeilenindex**, der Index der Zeile, ab der die neuen Zeilen eingefügt werden
- **Anzahl der Zeilen**, Gesamtanzahl der einzufügenden Zeilen

{{< highlight csharp >}}

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
Entwickler können eine Zeile aus dem Arbeitsblatt an beliebiger Stelle löschen, indem sie die **DeleteRow**-Methode der Cells-Sammlung aufrufen. Die **DeleteRow**-Methode nimmt den Index der Zeile an, die gelöscht werden soll.

{{< highlight csharp >}}

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
## **Mehrere Zeilen löschen**
Wenn Entwickler mehrere Zeilen aus dem Arbeitsblatt löschen müssen, kann dies auch durch Aufrufen der DeleteRows-Methode der Cells-Sammlung erfolgen. Die DeleteRows-Methode nimmt zwei Parameter an:

- **Zeilenindex**, der Index der Zeile, ab der die Zeilen gelöscht werden
- **Anzahl der Zeilen**, Gesamtanzahl der zu löschenden Zeilen

{{< highlight csharp >}}

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
Entwickler können auch eine Spalte in das Arbeitsblatt an beliebiger Stelle einfügen, indem sie die InsertColumn-Methode der Cells-Sammlung aufrufen.

{{< highlight csharp >}}

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
Um eine Spalte aus dem Arbeitsblatt an einer beliebigen Stelle zu löschen, können Entwickler die DeleteColumn-Methode der Cells-Sammlung aufrufen. Die DeleteColumn-Methode nimmt den Index der zu löschenden Spalte an.

{{< highlight csharp >}}

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
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Work%20with%20Rows%20n%20Columns%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
