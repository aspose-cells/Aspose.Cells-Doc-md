---
title: Spalten mit stark typisierten Daten
type: docs
weight: 20
url: /de/net/columns-containing-strongly-typed-data/
---

Wir wissen, dass eine Tabelle Daten als Sequenz von Zeilen und Spalten speichert. Wenn alle Werte in den Spalten eines Tabellenblatts stark typisiert sind (das bedeutet, dass alle Werte in einer Spalte den gleichen Datentyp haben müssen), dann können wir den Inhalt des Tabellenblatts exportieren, indem wir die Methode **ExportDataTable** der Cells-Klasse aufrufen. Die **ExportDataTable**-Methode nimmt die folgenden Parameter an, um die Daten des Tabellenblatts als **DataTable**-Objekt zu exportieren: **Zeilennummer** , repräsentiert die Zeilennummer der ersten Zelle, von der die Daten exportiert werden

- **Spaltennummer** , repräsentiert die Spaltennummer der ersten Zelle, von der die Daten exportiert werden
- **Anzahl der Zeilen** , repräsentiert die Anzahl der zu exportierenden Zeilen
- **Anzahl der Spalten** , repräsentiert die Anzahl der zu exportierenden Spalten
- **Spaltennamen exportieren** , eine boolesche Eigenschaft, die angibt, ob die Daten in der ersten Zeile des Tabellenblatts als Spaltennamen des DataTable exportiert werden sollen oder nicht

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(FOD_OpenFile.FileName, FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Exporting the contents of 2 rows and 2 columns starting from 1st cell to DataTable

DataTable dataTable = worksheet.Cells.ExportDataTable(0, 0,2, 2, true);

//Binding the DataTable with DataGrid

dataGridView1.DataSource = dataTable;

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
