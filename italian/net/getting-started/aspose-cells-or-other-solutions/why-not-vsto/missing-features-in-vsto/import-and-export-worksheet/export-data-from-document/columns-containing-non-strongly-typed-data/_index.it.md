---
title: Colonne che contengono dati non fortemente tipizzati
type: docs
weight: 10
url: /it/net/columns-containing-non-strongly-typed-data/
---

Se tutti i valori nelle colonne di un foglio di lavoro non sono fortemente tipizzati (ciò significa che i valori in una colonna possono avere tipi di dati diversi) allora possiamo esportare il contenuto del foglio di lavoro chiamando il metodo **ExportDataTableAsString** della classe Cells. Il metodo **ExportDataTableAsString** prende lo stesso set di parametri del metodo **ExportDataTable** per esportare i dati del foglio di lavoro come oggetto **DataTable**.

{{< highlight csharp >}}

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

Di seguito sono riportate le schermate:

![todo:image_alt_text](picture1.png)

![todo:image_alt_text](picture2.png)

## **Scarica il codice di esempio**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Export.from.Worksheet.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Export%20from%20Worksheet%20%28Aspose.Cells%29.zip)
