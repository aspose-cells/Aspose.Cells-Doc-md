---
title: Mostrar u ocultar encabezados de columna de fila en Aspose.Cells
type: docs
weight: 60
url: /es/net/display-or-hide-row-column-headers-in-aspose-cells/
---
{{% alert color="primary" %}}

Todas las hojas de trabajo en un archivo de Excel se componen de celdas que se organizan en filas y columnas. Todas las filas y columnas tienen valores únicos que se utilizan para identificarlas y para identificar celdas individuales. Por ejemplo, las filas están numeradas (1, 2, 3, 4, etc.) y las columnas están ordenadas alfabéticamente (A, B, C, D, etc.). Los valores de fila y columna se muestran en los encabezados. Usando Aspose.Cells, los desarrolladores pueden controlar la visibilidad de estos encabezados de fila y columna.

{{% /alert %}}

## **Control de la visibilidad de las hojas de trabajo**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , que representa un archivo de Excel Microsoft. Él[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)colección que permite el acceso a cada hoja de trabajo en un archivo de Excel.

 Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. Él[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) La clase proporciona una amplia gama de propiedades y métodos para administrar hojas de trabajo. Para controlar la visibilidad de los encabezados de fila y columna, use el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase'[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) propiedad.[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) es una propiedad booleana, lo que significa que solo puede almacenar una**verdadero** o**falso** valor.

 A continuación se muestra un ejemplo completo que muestra cómo utilizar el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase'[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) propiedad para ocultar los encabezados de fila y columna en la primera hoja de cálculo de un archivo.

La captura de pantalla muestra Book1.xls, el archivo de entrada. Contiene tres hojas de trabajo: Hoja1, Hoja2 y Hoja3. Cada hoja de trabajo muestra encabezados de fila y columna.

**Book1.xls: hoja de trabajo antes de la modificación**

![todo:imagen_alternativa_texto](display-or-hide-row-column-headers-in-aspose-cells_1.png)

Book1.xls se abre llamando al método Open de la clase Workbook y los encabezados de fila y columna en la primera hoja de trabajo están ocultos. El archivo modificado se guarda como salida.xls.

**Output.xls: hoja de trabajo después de la modificación** 

![todo:imagen_alternativa_texto](display-or-hide-row-column-headers-in-aspose-cells_2.png)

**C#**

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Hiding the headers of rows and columns

worksheet.IsRowColumnHeadersVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **Descargar código de ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Row%20Column%20Headers)

## **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
