---
title: Colonne contenenti dati fortemente tipizzati
type: docs
weight: 20
url: /it/net/columns-containing-strongly-typed-data/
---
 Sappiamo che un foglio di calcolo memorizza i dati come una sequenza di righe e colonne. Se tutti i valori nelle colonne di un foglio di lavoro sono fortemente tipizzati (ciò significa che tutti i valori in una colonna devono avere lo stesso tipo di dati), allora possiamo esportare il contenuto del foglio di lavoro chiamando il**ExportDataTable** metodo della classe Cells.**ExportDataTable** Il metodo accetta i seguenti parametri per esportare i dati del foglio di lavoro come**Tabella dati** oggetto:**Numero riga** , rappresenta il numero di riga della prima cella da cui verranno esportati i dati

- **Numero di colonna** , rappresenta il numero di colonna della prima cella da cui verranno esportati i dati
- **Numero di righe** , rappresenta il numero di righe da esportare
- **Numero di colonne** rappresenta il numero di colonne da esportare
- **Esporta nomi di colonne** , una proprietà booleana che indica se i dati nella prima riga del foglio di lavoro devono essere esportati o meno come nomi di colonna della DataTable

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
