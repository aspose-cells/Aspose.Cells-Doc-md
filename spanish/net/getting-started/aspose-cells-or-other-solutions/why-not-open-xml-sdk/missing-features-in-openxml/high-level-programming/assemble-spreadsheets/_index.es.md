---
title: Ensamblar Hojas de Cálculo
type: docs
weight: 10
url: /es/net/assemble-spreadsheets/
---

Esta sección describe cómo:

Crear un nuevo archivo de Excel desde cero y agregar una hoja de trabajo.

- Agregar hojas de trabajo a hojas de cálculo diseñadas.
- Acceda a las hojas de cálculo utilizando el nombre de la hoja.
- Elimine una hoja de cálculo de un archivo de Excel utilizando su nombre de hoja.
- Elimine una hoja de cálculo de un archivo de Excel utilizando su índice de hoja.
- Aspose.Cells proporciona una clase, Workbook que representa un archivo de Excel. La clase Workbook contiene una colección de Worksheets que permite el acceso a cada hoja de cálculo en el archivo de Excel.

Una hoja de cálculo está representada por la clase Worksheet. La clase Worksheet proporciona una amplia gama de propiedades y métodos para administrar las hojas de cálculo.
## **Añadir hojas de cálculo a un nuevo archivo de Excel**
Para crear un nuevo archivo de Excel programáticamente:

- Cree un objeto de la clase Workbook.
- Llame al método Add de la colección Worksheets. Se agrega automáticamente una hoja de cálculo vacía al archivo de Excel. Se puede hacer referencia pasando el índice de hoja de cálculo de la nueva hoja de cálculo a la colección Worksheets.
- Obtener una referencia de la hoja de cálculo.
- Realizar trabajo en las hojas de cálculo.
- Guarde el nuevo archivo de Excel con nuevas hojas de cálculo llamando al método Save de la clase Workbook.

{{< highlight csharp >}}

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
## **Añadir hojas de cálculo a una hoja de cálculo de diseñador**
El proceso de añadir hojas de cálculo a una hoja de cálculo de diseñador es el mismo que el de añadir una nueva hoja de cálculo, excepto que el archivo de Excel ya existe, por lo que debe abrirse antes de que se añadan las hojas de cálculo. Una hoja de cálculo de diseñador puede abrirse mediante la clase Workbook.

{{< highlight csharp >}}

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
## **Acceso a las hojas de cálculo usando el nombre de la hoja**
Acceda o obtenga cualquier hoja de cálculo especificando su nombre o índice.

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing a worksheet using its sheet name

Worksheet worksheet = workbook.Worksheets["Sheet1"];

{{< /highlight >}}
## **Eliminar hojas de cálculo utilizando el nombre de la hoja**
Para eliminar hojas de cálculo de un archivo, llame al método RemoveAt de la colección Worksheets. Pase el nombre de la hoja al método RemoveAt para eliminar una hoja de cálculo específica.

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet name

workbook.Worksheets.RemoveAt("Sheet3");

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **Eliminar hojas de cálculo utilizando el índice de la hoja**
Eliminar hojas de cálculo por nombre funciona bien cuando se conoce el nombre de la hoja de cálculo. Si no conoce el nombre de la hoja de cálculo, utilice una versión sobrecargada del método RemoveAt que tome el índice de la hoja de cálculo en lugar de su nombre de hoja.

{{< highlight csharp >}}

 //creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet index

workbook.Worksheets.RemoveAt(1);

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **Descargar Código de Ejemplo**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Assemble%20Worksheet%20%28Aspose.Cells%29.zip)
