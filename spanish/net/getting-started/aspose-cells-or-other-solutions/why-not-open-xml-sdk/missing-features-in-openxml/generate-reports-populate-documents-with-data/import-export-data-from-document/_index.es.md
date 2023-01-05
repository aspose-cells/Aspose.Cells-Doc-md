---
title: Importar Exportar datos del documento
type: docs
weight: 10
url: /es/net/import-export-data-from-document/
---
## **Importar datos del documento**

Los datos son la recopilación de hechos en bruto y creamos documentos o informes de hojas de cálculo para presentar estos hechos en bruto de una manera más significativa. Normalmente, agregamos datos a las hojas de cálculo nosotros mismos, pero a veces necesitamos reutilizar los recursos de datos existentes y aquí surge la necesidad de importar datos a las hojas de cálculo desde diferentes fuentes de datos. En este tema, discutiremos algunas técnicas para importar datos a hojas de trabajo desde diferentes fuentes de datos.

## **Importación de datos usando Aspose.Cells**

 cuando usas**Aspose.Cells** para abrir un archivo de Excel, todos los datos del archivo se importan automáticamente, pero Aspose.Cells también admite la importación de datos de diferentes fuentes de datos. Algunas de estas fuentes de datos se enumeran a continuación:

- **Formación**
- **Lista de arreglo**
- **Tabla de datos**
- **Columna de datos**
- **vista de datos**
- **Cuadrícula de datos**
- **Lector de datos**
- **Vista en cuadrícula**

 Aspose.Cells proporciona una clase,**Libro de trabajo** que representa un archivo de Excel. La clase de libro de trabajo contiene una colección de hojas de trabajo que permite acceder a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por la clase Worksheet. La clase Worksheet proporciona una colección Cells.

La colección Cells proporciona métodos muy útiles para importar datos de diferentes fuentes de datos.

### **Importación desde matriz**

 Los desarrolladores pueden importar datos de una matriz a sus hojas de trabajo llamando al**Importar matriz** método de la colección Cells. Hay muchas versiones sobrecargadas del método ImportArray pero una sobrecarga típica toma los siguientes parámetros:

- Array, representa el objeto de matriz cuyo contenido necesita importar
- Número de fila, representa el número de fila de la primera celda donde se importarán los datos
- Número de columna, representa el número de columna de la primera celda donde se importarán los datos
- Es Vertical, un valor booleano que especifica importar datos vertical u horizontalmente

{{< highlight "csharp" >}}

//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Creating an array containing names as string values

string[]names = new string[]{ "laurence chen", "roman korchagin", "kyle huang" };

//Importing the array of names to 1st row and first column vertically

worksheet.Cells.ImportArray(names, 0, 0, true);

//Saving the Excel file

workbook.Save(MyDir+"DataImport from Array.xls");

{{< /highlight >}}

### **Importando desde ArrayList**

 Los desarrolladores pueden importar datos de un ArrayList a sus hojas de trabajo llamando al**Importar ArrayList** método de la colección Cells. El método ImportArray toma los siguientes parámetros:**Lista de arreglo** , representa el objeto ArrayList cuyo contenido necesita importar

- Número de fila, representa el número de fila de la primera celda donde se importarán los datos
- Número de columna, representa el número de columna de la primera celda donde se importarán los datos
- Es Vertical , un valor booleano que especifica importar datos vertical u horizontalmente

{{< highlight "csharp" >}}

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

### **Importación desde objetos personalizados**

 Los desarrolladores pueden importar datos de la colección de objetos a una hoja de trabajo usando**Importar objetos personalizados**. Puede proporcionar una lista de columnas/propiedades al método para mostrar la lista de objetos deseada.

{{< highlight "csharp" >}}

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

new string[]{ "Date", "InWIPStage", "Shipment", "Payment" },

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

### **Importando desde DataTable**

 Los desarrolladores pueden importar datos desde un**Tabla de datos** a sus hojas de trabajo llamando al**ImportDataTable** método de la colección Cells. Hay muchas versiones sobrecargadas del**ImportDataTable** pero una sobrecarga típica toma los siguientes parámetros:**Tabla de datos** , representa el**Tabla de datos** objeto cuyo contenido necesita importar

- **¿Se muestra el nombre del campo?**, especifica si los nombres de las columnas de DataTable deben importarse a la hoja de trabajo como una primera fila o no
- **Inicio Cell** representa el nombre de la celda de inicio (es decir, "A1") desde donde importar el contenido de DataTable

{{< highlight "csharp" >}}

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

dr[0]= 1;

dr[1]= "Aniseed Syrup";

dr[2]= 15;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Creating another empty row in the DataTable object

dr = dataTable.NewRow();

//Adding data to the row

dr[0]= 2;

dr[1]= "Boston Crab Meat";

dr[2]= 123;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Importing the contents of DataTable to the worksheet starting from "A1" cell,

//where true specifies that the column names of the DataTable would be added to

//the worksheet as a header row

worksheet.Cells.ImportDataTable(dataTable, true, "A1");

workbook.Save(MyDir+"Import From Data Table.xls");

{{< /highlight >}}

## **Descargar código de muestra**

- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Import%20to%20Worksheet%20%28Aspose.Cells%29.zip)

## **Exportar datos del documento**

 Aspose.Cells no solo facilita a sus usuarios importar datos a hojas de trabajo desde fuentes de datos externas, sino que también les permite exportar sus datos de hojas de trabajo a un**Tabla de datos** . Como sabemos que**Tabla de datos** es la parte de ADO.NET y se utiliza para almacenar datos. Una vez que los datos se almacenan en un**Tabla de datos**, se puede utilizar de cualquier manera según los requisitos de los usuarios.

## **Exportación de datos a DataTable (.NET) usando Aspose.Cells**

Los desarrolladores pueden exportar fácilmente los datos de su hoja de cálculo a un objeto DataTable llamando al método ExportDataTable o ExportDataTableAsString de la clase Cells. Ambos métodos se utilizan en diferentes escenarios, que se analizan a continuación con más detalle.

### **Columnas que contienen datos fuertemente tipados**

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

### **Columnas que contienen datos no fuertemente tipados**

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

## **Descargar código de muestra**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Export%20from%20Worksheet%20%28Aspose.Cells%29.zip)
