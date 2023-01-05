---
title: ensamblar hojas de cálculo
type: docs
weight: 10
url: /es/net/assemble-spreadsheets/
---
Esta sección describe cómo:

Cree un nuevo archivo de Excel desde cero y agréguele una hoja de trabajo.

- Agregue hojas de trabajo a las hojas de cálculo del diseñador.
- Acceda a las hojas de trabajo usando el nombre de la hoja.
- Elimine una hoja de trabajo de un archivo de Excel usando su nombre de hoja.
- Elimine una hoja de trabajo de un archivo de Excel usando su índice de hoja.
- Aspose.Cells proporciona una clase, Workbook, que representa un archivo de Excel. La clase Libro de trabajo contiene una colección de Hojas de trabajo que permite acceder a cada hoja de trabajo en el archivo de Excel.

Una hoja de trabajo está representada por la clase Worksheet. La clase Worksheet proporciona una amplia gama de propiedades y métodos para administrar hojas de trabajo.
## **Agregar hojas de trabajo a un nuevo archivo de Excel**
Para crear un nuevo archivo de Excel mediante programación:

- Cree un objeto de la clase Workbook.
- Llame al método Add de la colección Worksheets. Una hoja de trabajo vacía se agrega al archivo de Excel * automáticamente. Se puede hacer referencia a ella pasando el índice de hoja de la nueva hoja de trabajo a la colección Hojas de trabajo.
- Obtenga una referencia de la hoja de trabajo.
- Realizar el trabajo en las hojas de trabajo.
- Guarde el nuevo archivo de Excel con nuevas hojas de trabajo llamando al método Guardar de la clase Workbook.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Setting the name of the newly added worksheet

worksheet.Name = "My Worksheet";

//Saving the Excel file

workbook.Save("Adding Worksheet.xls");

{{< /highlight >}}
## **Adición de hojas de trabajo a una hoja de cálculo de Designer**
El proceso de agregar hojas de trabajo a una hoja de cálculo de diseñador es el mismo que el de agregar una nueva hoja de trabajo, excepto que el archivo de Excel ya existe, por lo que debe abrirse antes de agregar las hojas de trabajo. La clase Workbook puede abrir una hoja de cálculo de diseñador.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Setting the name of the newly added worksheet

worksheet.Name = "My Worksheet";

//Saving the Excel file

workbook.Save("Designer Spreadsheet.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Acceder a las hojas de trabajo usando el nombre de la hoja**
Acceda u obtenga cualquier hoja de trabajo especificando su nombre o índice.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing a worksheet using its sheet name

Worksheet worksheet = workbook.Worksheets["Sheet1"];

{{< /highlight >}}
## **Eliminación de hojas de trabajo usando el nombre de la hoja**
Para eliminar hojas de trabajo de un archivo, llame al método RemoveAt de la colección Worksheets. Pase el nombre de la hoja al método RemoveAt para eliminar una hoja de trabajo específica.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet name

workbook.Worksheets.RemoveAt("Sheet3");

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **Eliminación de hojas de cálculo mediante el índice de hojas**
La eliminación de hojas de trabajo por nombre funciona bien cuando se conoce el nombre de la hoja de trabajo. Si no conoce el nombre de la hoja de trabajo, use una versión sobrecargada del método RemoveAt que toma el índice de la hoja de trabajo en lugar de su nombre de hoja.

{{< highlight "csharp" >}}

 //creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet index

workbook.Worksheets.RemoveAt(1);

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **Descargar código de muestra**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Assemble%20Worksheet%20%28Aspose.Cells%29.zip)
