---
title: Spalten mit nicht stark typisierten Daten
type: docs
weight: 10
url: /de/net/columns-containing-non-strongly-typed-data/
---
 Wenn alle Werte in den Spalten eines Arbeitsblatts nicht stark typisiert sind (d. h. die Werte in einer Spalte können unterschiedliche Datentypen haben), können wir den Inhalt des Arbeitsblatts exportieren, indem wir die aufrufen**ExportDataTableAsString** Methode der Klasse Cells.**ExportDataTableAsString** Die Methode verwendet denselben Satz von Parametern wie die von**ExportDataTable** Methode zum Exportieren von Arbeitsblattdaten als**Datentabelle** Objekt.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(FOD_OpenFile.FileName, FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Exporting the contents of 2 rows and 2 columns starting from 1st cell to DataTable

DataTable dataTable = worksheet.Cells.ExportDataTableAsString(0, 0, 2, 2, true);

//Binding the DataTable with DataGrid

dataGridView2.DataSource = dataTable;

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

Nachfolgend die Screenshots:

![todo: Bild_alt_Text](picture1.png)

![todo: Bild_alt_Text](picture2.png)

## **Beispielcode herunterladen**

- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Export.from.Worksheet.Aspose.Cells.zip)
- [Bit Bucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Export%20from%20Worksheet%20%28Aspose.Cells%29.zip)
