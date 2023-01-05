---
title: Spalten mit stark typisierten Daten
type: docs
weight: 20
url: /de/net/columns-containing-strongly-typed-data/
---
Wir wissen, dass eine Tabelle Daten als eine Folge von Zeilen und Spalten speichert. Wenn alle Werte in den Spalten eines Arbeitsblatts stark typisiert sind (d. h. alle Werte in einer Spalte müssen denselben Datentyp haben), können wir den Inhalt des Arbeitsblatts exportieren, indem wir die aufrufen**ExportDataTable** Methode der Klasse Cells.**ExportDataTable** -Methode verwendet die folgenden Parameter, um Arbeitsblattdaten als zu exportieren**Datentabelle** Objekt:**Zeilennummer** , stellt die Zeilennummer der ersten Zelle dar, aus der die Daten exportiert werden

- **Spaltennummer** , stellt die Spaltennummer der ersten Zelle dar, aus der die Daten exportiert werden
- **Anzahl der Reihen** , stellt die Anzahl der zu exportierenden Zeilen dar
- **Anzahl der Spalten** stellt die Anzahl der zu exportierenden Spalten dar
- **Spaltennamen exportieren** , eine boolesche Eigenschaft, die angibt, ob die Daten in der ersten Zeile des Arbeitsblatts als Spaltennamen der DataTable exportiert werden sollen oder nicht

{{< highlight "csharp" >}}

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
