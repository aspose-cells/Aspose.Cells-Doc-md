---
title: Columnas que contienen datos tipificados
type: docs
weight: 20
url: /es/net/columns-containing-strongly-typed-data/
---

Sabemos que una hoja de cálculo almacena datos como una secuencia de filas y columnas. Si todos los valores en las columnas de una hoja de cálculo están fuertemente tipados (es decir, todos los valores en una columna deben tener el mismo tipo de datos), entonces podemos exportar el contenido de la hoja de cálculo llamando al método **ExportDataTable** de la clase Cells. El método **ExportDataTable** toma los siguientes parámetros para exportar los datos de la hoja de cálculo como un objeto **DataTable**: **Número de Fila** , representa el número de fila de la primera celda desde donde se exportarán los datos

- **Número de Columna** , representa el número de columna de la primera celda desde donde se exportarán los datos
- **Número de Filas** , representa el número de filas a exportar
- **Número de Columnas** , representa el número de columnas a exportar
- **Exportar Nombres de Columna** , una propiedad booleana que indica si los datos en la primera fila de la hoja de cálculo deben ser exportados como nombres de columna del DataTable o no

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
{{< app/cells/assistant language="csharp" >}}
