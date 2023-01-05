---
title: Columnas que contienen datos fuertemente tipados
type: docs
weight: 20
url: /es/net/columns-containing-strongly-typed-data/
---
Sabemos que una hoja de cálculo almacena datos como una secuencia de filas y columnas. Si todos los valores en las columnas de una hoja de trabajo están fuertemente tipados (eso significa que todos los valores en una columna deben tener el mismo tipo de datos), entonces podemos exportar el contenido de la hoja de trabajo llamando a la**ExportDataTableExportDataTable** método de la clase Cells.**ExportDataTableExportDataTable** El método toma los siguientes parámetros para exportar datos de la hoja de trabajo como**Tabla de datos** objeto:**Numero de fila** , representa el número de fila de la primera celda desde donde se exportarán los datos

- **Número de columna** , representa el número de columna de la primera celda desde donde se exportarán los datos
- **Número de filas** , representa el número de filas a exportar
- **Número de columnas** representa el número de columnas a exportar
- **Exportar nombres de columnas** , una propiedad booleana que indica si los datos en la primera fila de la hoja de trabajo deben exportarse como nombres de columna de DataTable o no

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
