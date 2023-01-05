---
title: Columnas que contienen datos no fuertemente tipados
type: docs
weight: 10
url: /es/net/columns-containing-non-strongly-typed-data/
---
 Si todos los valores en las columnas de una hoja de trabajo no están fuertemente tipados (eso significa que los valores en una columna pueden tener diferentes tipos de datos), entonces podemos exportar el contenido de la hoja de trabajo llamando a la**ExportDataTableAsStringExportDataTableAsString** método de la clase Cells.**ExportDataTableAsStringExportDataTableAsString** El método toma el mismo conjunto de parámetros que el de**ExportDataTableExportDataTable** método para exportar datos de la hoja de trabajo como**Tabla de datos** objeto.

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

A continuación se muestran las capturas de pantalla:

![todo:imagen_alternativa_texto](picture1.png)

![todo:imagen_alternativa_texto](picture2.png)

## **Descargar código de muestra**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Export.from.Worksheet.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Export%20from%20Worksheet%20%28Aspose.Cells%29.zip)
