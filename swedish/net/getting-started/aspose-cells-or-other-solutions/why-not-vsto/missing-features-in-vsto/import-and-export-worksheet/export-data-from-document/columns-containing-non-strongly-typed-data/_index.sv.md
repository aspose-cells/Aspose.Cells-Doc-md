---
title: Kolumner som innehåller icke-starkt typade data
type: docs
weight: 10
url: /sv/net/columns-containing-non-strongly-typed-data/
---
 Om alla värden i kolumnerna i ett kalkylblad inte är starkt skrivna (det betyder att värdena i en kolumn kan ha olika datatyper) så kan vi exportera kalkylbladets innehåll genom att anropa**ExportDataTableAsString** metod av klassen Cells.**ExportDataTableAsString** metoden tar samma uppsättning parametrar som den för**ExportDataTable** metod för att exportera kalkylbladsdata som**Datatabell** objekt.

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

Nedan är skärmdumparna:

![todo:image_alt_text](picture1.png)

![todo:image_alt_text](picture2.png)

## **Ladda ner exempelkod**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Export.from.Worksheet.Aspose.Cells.zip)
- [Bit hink](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Export%20from%20Worksheet%20%28Aspose.Cells%29.zip)
