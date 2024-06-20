---
title: Mostrar u Ocultar Líneas de Cuadrícula en Aspose.Cells
type: docs
weight: 50
url: /es/net/display-or-hide-gridlines-in-aspose-cells/
---

{{% alert color="primary" %}}

Todas las hojas de cálculo de Excel tienen líneas de cuadrícula de forma predeterminada. Ayudan a delimitar las celdas, de modo que sea fácil ingresar datos en celdas específicas. Las líneas de la cuadrícula nos permiten ver una hoja de cálculo como una colección de celdas, donde cada celda es fácilmente identificable.

{{% /alert %}}

## **Controlar la visibilidad de las cuadrículas**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) que permite acceder a cada hoja de cálculo en el archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona una amplia gama de propiedades y métodos para gestionar una hoja de cálculo. Para controlar la visibilidad de las líneas de cuadrícula, use la propiedad [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) de la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) es una propiedad booleana, lo que significa que solo puede almacenar un valor **true** o **false**.

A continuación se muestra un ejemplo completo que demuestra el uso de la propiedad [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) de la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) para ocultar las líneas de cuadrícula de la primera hoja de cálculo del archivo de Excel.

En la captura de pantalla a continuación, se puede ver que el archivo Book1.xls contiene tres hojas de cálculo: Hoja1, Hoja2 y Hoja3. Todas las hojas de cálculo tienen líneas de cuadrícula.

**Book1.xls: vista de la hoja de cálculo antes de la modificación** 

![todo:image_alt_text](display-or-hide-gridlines-in-aspose-cells_1.png)

El archivo Book1.xls se abre utilizando la clase Workbook y las líneas de cuadrícula en la primera hoja de cálculo se ocultan. El archivo modificado se guarda como output.xls.

**Output.xls: hoja de cálculo después de la modificación** 

![todo:image_alt_text](display-or-hide-gridlines-in-aspose-cells_2.png)

**C#**

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Hiding the gridlines of the first worksheet of the Excel file

worksheet.IsGridlinesVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **Descargar Código en Ejecución**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Gridlines)

## **Descargar Código de Ejemplo**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
