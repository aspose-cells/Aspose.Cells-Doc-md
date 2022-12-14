---
title: Mostrar u ocultar líneas de cuadrícula en Aspose.Cells
type: docs
weight: 50
url: /es/net/display-or-hide-gridlines-in-aspose-cells/
---
{{% alert color="primary" %}}

Todas las hojas de cálculo de Excel tienen líneas de cuadrícula de forma predeterminada. Ayudan a delinear las celdas, de modo que es fácil ingresar datos en celdas particulares. Las líneas de cuadrícula nos permiten ver una hoja de trabajo como una colección de celdas, donde cada celda es fácilmente identificable.

{{% /alert %}}

## **Controlar la visibilidad de las líneas de cuadrícula**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) colección que permite el acceso a cada hoja de trabajo en el archivo de Excel.

 Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. los[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) La clase proporciona una amplia gama de propiedades y métodos para administrar una hoja de cálculo. Para controlar la visibilidad de las líneas de cuadrícula, utilice el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase'[**EsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) propiedad.[**EsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) es una propiedad booleana, lo que significa que solo puede almacenar una**verdadero** o**falso** valor.

 A continuación se muestra un ejemplo completo que demuestra el uso de la[**EsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) propiedad de la[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class para ocultar las líneas de cuadrícula de la primera hoja de cálculo del archivo de Excel.

En la siguiente captura de pantalla, puede ver que el archivo Book1.xls contiene tres hojas de trabajo: Sheet1, Sheet2 y Sheet3. Todas las hojas de trabajo tienen líneas de cuadrícula.

**Book1.xls: vista de la hoja de trabajo antes de la modificación** 

![todo:imagen_alternativa_texto](display-or-hide-gridlines-in-aspose-cells_1.png)

El archivo Book1.xls se abre con la clase Workbook y las líneas de cuadrícula de la primera hoja de trabajo están ocultas. El archivo modificado se guarda como salida.xls.

**Output.xls: hoja de trabajo después de la modificación** 

![todo:imagen_alternativa_texto](display-or-hide-gridlines-in-aspose-cells_2.png)

**C#**

{{< highlight "csharp" >}}

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

## **Descargar código de ejecución**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Gridlines)

## **Descargar código de muestra**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
