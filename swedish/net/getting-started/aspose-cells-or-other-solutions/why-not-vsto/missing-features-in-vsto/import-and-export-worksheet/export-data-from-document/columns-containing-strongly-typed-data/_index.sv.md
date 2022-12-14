---
title: Kolumner som innehåller starkt skrivna data
type: docs
weight: 20
url: /sv/net/columns-containing-strongly-typed-data/
---
 Vi vet att ett kalkylblad lagrar data som en sekvens av rader och kolumner. Om alla värden i kolumnerna i ett kalkylblad är starkt skrivna (det betyder att alla värden i en kolumn måste ha samma datatyp) kan vi exportera kalkylbladets innehåll genom att anropa**ExportDataTable** metod av klassen Cells.**ExportDataTable** metod använder följande parametrar för att exportera kalkylbladsdata som**Datatabell** objekt:**Radnummer** , representerar radnumret för den första cellen varifrån data kommer att exporteras

- **Kolumnnummer** , representerar kolumnnumret för den första cellen varifrån data kommer att exporteras
- **Antal rader** , representerar antalet rader som ska exporteras
- **Antal kolumner** representerar antalet kolumner som ska exporteras
- **Exportera kolumnnamn** , en boolesk egenskap som anger om data i första raden i kalkylbladet ska exporteras som kolumnnamn i datatabellen eller inte

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
