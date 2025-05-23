---
title: Importar desde DataTable
type: docs
weight: 40
url: /es/net/importing-from-datatable/
---

Los desarrolladores pueden importar datos desde un **DataTable** a sus hojas de cálculo llamando al método **ImportDataTable** de la colección Cells. Hay muchas versiones sobrecargadas del método **ImportDataTable** pero una sobrecarga típica toma los siguientes parámetros: **DataTable** , representa el objeto **DataTable** cuyo contenido necesita ser importado

- **¿Se Muestra el Nombre del Campo?**, especifica si los nombres de las columnas de DataTable deben ser importados a la hoja de cálculo como primera fila o no
- **Celda de Inicio** , representa el nombre de la celda de inicio (es decir, "A1") desde donde importar el contenido del DataTable

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Instantiating a "Products" DataTable object

DataTable dataTable = new DataTable("Products");

//Adding columns to the DataTable object

dataTable.Columns.Add("Product ID", typeof(Int32));

dataTable.Columns.Add("Product Name", typeof(string));

dataTable.Columns.Add("Units In Stock", typeof(Int32));

//Creating an empty row in the DataTable object

DataRow dr = dataTable.NewRow();

//Adding data to the row

dr[0] = 1;

dr[1] = "Aniseed Syrup";

dr[2] = 15;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Creating another empty row in the DataTable object

dr = dataTable.NewRow();

//Adding data to the row

dr[0] = 2;

dr[1] = "Boston Crab Meat";

dr[2] = 123;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Importing the contents of DataTable to the worksheet starting from "A1" cell,

//where true specifies that the column names of the DataTable would be added to

//the worksheet as a header row

worksheet.Cells.ImportDataTable(dataTable, true, "A1");

workbook.Save("Import From Data Table.xls");

{{< /highlight >}}
## **Descargar Código de Ejemplo**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Import.to.Worksheet.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Import%20to%20Worksheet%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
