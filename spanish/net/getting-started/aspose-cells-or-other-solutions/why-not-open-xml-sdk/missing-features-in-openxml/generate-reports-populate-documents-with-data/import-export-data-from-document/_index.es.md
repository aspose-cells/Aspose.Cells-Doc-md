---
title: Importar Exportar datos desde documento
type: docs
weight: 10
url: /es/net/import-export-data-from-document/
---

## **Importar datos desde documento**

Los datos son la colección de hechos crudos y creamos documentos de hojas de cálculo o informes para presentar estos hechos crudos de una manera más significativa. Normalmente, agregamos datos a hojas de cálculo por nosotros mismos, pero a veces, necesitamos reutilizar recursos de datos existentes y aquí es donde surge la necesidad de importar datos a hojas de cálculo desde diferentes fuentes de datos. En este tema, discutiremos algunas técnicas para importar datos a hojas de cálculo desde diferentes fuentes de datos.

## **Importar Datos Usando Aspose.Cells**

Cuando se utiliza **Aspose.Cells** para abrir un archivo de Excel, todos los datos en el archivo se importan automáticamente, pero Aspose.Cells también admite la importación de datos desde diferentes fuentes de datos. Algunas de estas fuentes de datos se enumeran a continuación:

- **Array**
- **ArrayList**
- **DataTable**
- **DataColumn**
- **DataView**
- **DataGrid**
- **DataReader**
- **GridView**

Aspose.Cells proporciona una clase, **Workbook** que representa un archivo de Excel. La clase Workbook contiene una colección de Worksheets que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase Worksheet. La clase Worksheet proporciona una colección de Cells.

La colección de Cells proporciona métodos muy útiles para importar datos de diferentes fuentes de datos.

### **Importar desde un Arreglo**

Los desarrolladores pueden importar datos desde un array a sus hojas de cálculo llamando al método **ImportArray** de la colección Cells. Hay muchas versiones sobrecargadas del método ImportArray, pero una sobrecarga típica toma los siguientes parámetros:

- Array, representa el objeto array cuyo contenido necesita ser importado
- Número de fila, representa el número de fila de la primera celda donde se importarán los datos
- Número de columna, representa el número de columna de la primera celda donde se importarán los datos
- Es Vertical, un valor booleano que especifica si importar los datos vertical u horizontalmente

{{< highlight csharp >}}

//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Creating an array containing names as string values

string[] names = new string[] { "laurence chen", "roman korchagin", "kyle huang" };

//Importing the array of names to 1st row and first column vertically

worksheet.Cells.ImportArray(names, 0, 0, true);

//Saving the Excel file

workbook.Save(MyDir+"DataImport from Array.xls");

{{< /highlight >}}

### **Importar desde un ArrayList**

Los desarrolladores pueden importar datos desde un ArrayList a sus hojas de cálculo llamando al método **ImportArrayList** de la colección Cells. El método ImportArrayList toma los siguientes parámetros: **ArrayList**, representa el objeto ArrayList cuyo contenido necesita ser importado

- Número de fila, representa el número de fila de la primera celda donde se importarán los datos
- Número de columna, representa el número de columna de la primera celda donde se importarán los datos
- Es Vertical, un valor booleano que especifica si importar los datos vertical u horizontalmente

{{< highlight csharp >}}

//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Instantiating an ArrayList object

ArrayList list = new ArrayList();

//Add few names to the list as string values

list.Add("laurence chen");

list.Add("roman korchagin");

list.Add("kyle huang");

list.Add("tommy wang");

//Importing the contents of ArrayList to 1st row and first column vertically

worksheet.Cells.ImportArrayList(list, 0, 0, true);

//Saving the Excel file

workbook.Save(MyDir + "DataImport from Array List.xls");

{{< /highlight >}}

### **Importar desde Objetos Personalizados**

Los desarrolladores pueden importar datos desde una colección de objetos a una hoja de cálculo usando **ImportCustomObjects**. Se puede proporcionar una lista de columnas/propiedades al método para mostrar la lista deseada de objetos.

{{< highlight csharp >}}

//Instantiate a new Workbook

Workbook book = new Workbook();

//Clear all the worksheets

book.Worksheets.Clear();

//Add a new Sheet "Data";

Worksheet sheet = book.Worksheets.Add("Data");

//Define List

List<WeeklyItem> list = new List<WeeklyItem>();

//Add data to the list of objects

list.Add(new WeeklyItem() { AtYarnStage = 1, InWIPStage = 2, Payment = 3, Shipment = 4, Shipment2 = 5 });

list.Add(new WeeklyItem() { AtYarnStage = 5, InWIPStage = 9, Payment = 7, Shipment = 2, Shipment2 = 5 });

list.Add(new WeeklyItem() { AtYarnStage = 7, InWIPStage = 3, Payment = 3, Shipment = 8, Shipment2 = 3 });

//We pick a few columns not all to import to the worksheet

sheet.Cells.ImportCustomObjects((System.Collections.ICollection)list,

new string[] { "Date", "InWIPStage", "Shipment", "Payment" },

true,

0,

0,

list.Count,

true,

"dd/mm/yyyy",

false);

//Auto-fit all the columns

book.Worksheets[0].AutoFitColumns();

//Save the Excel file

book.Save(MyDir+"ImportedCustomObjects.xls");

{{< /highlight >}}

### **Importar desde un DataTable**

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

workbook.Save(MyDir+"Import From Data Table.xls");

{{< /highlight >}}

## **Descargar Código de Ejemplo**

- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Import%20to%20Worksheet%20%28Aspose.Cells%29.zip)

## **Exportar datos desde el documento**

Aspose.Cells no solo facilita a sus usuarios importar datos a las hojas de cálculo desde fuentes de datos externas, sino que también les permite exportar sus datos de hojas de cálculo a un **DataTable**. Como sabemos que **DataTable** es parte de ADO.NET y se usa para almacenar datos. Una vez que los datos se almacenan en un **DataTable**, pueden utilizarse de cualquier manera según los requisitos de los usuarios.

## **Exportando Datos a DataTable (.NET) Usando Aspose.Cells**

Los desarrolladores pueden exportar fácilmente los datos de sus hojas de cálculo a un objeto DataTable llamando al método ExportDataTable o ExportDataTableAsString de la clase Cells. Ambos métodos se utilizan en diferentes escenarios, que se discuten con más detalle a continuación.

### **Columnas que contienen datos fuertemente tipados**

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

### **Columnas que contienen datos no fuertemente tipados**

Si todos los valores en las columnas de una hoja de cálculo no están fuertemente tipados (es decir, los valores en una columna pueden tener diferentes tipos de datos), entonces podemos exportar el contenido de la hoja de cálculo llamando al método **ExportDataTableAsString** de la clase Cells. El método **ExportDataTableAsString** toma el mismo conjunto de parámetros que el método **ExportDataTable** para exportar los datos de la hoja de cálculo como un objeto **DataTable**.

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

## **Descargar Código de Ejemplo**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Export%20from%20Worksheet%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
