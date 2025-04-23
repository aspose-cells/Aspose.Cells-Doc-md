---
title: Mostrar u Ocultar Encabezados de Filas y Columnas en Aspose.Cells
type: docs
weight: 60
url: /es/net/display-or-hide-row-column-headers-in-aspose-cells/
---

{{% alert color="primary" %}}

Todas las hojas de cálculo en un archivo de Excel están compuestas por celdas que se organizan en filas y columnas. Todas las filas y columnas tienen valores únicos que se utilizan para identificarlas, así como para identificar celdas individuales. Por ejemplo, las filas están numeradas – 1, 2, 3, 4, etc. – y las columnas están ordenadas alfabéticamente – A, B, C, D, etc. Los valores de fila y columna se muestran en los encabezados. Con Aspose.Cells, los desarrolladores pueden controlar la visibilidad de estos encabezados de fila y columna.

{{% /alert %}}

## **Controlar la visibilidad de las hojas de cálculo**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una colección de [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) que permite acceder a cada hoja de cálculo en un archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona una amplia gama de propiedades y métodos para gestionar hojas de cálculo. Para controlar la visibilidad de los encabezados de filas y columnas, utilice la propiedad [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) de la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) es una propiedad booleana, lo que significa que solo puede almacenar un valor **verdadero** o **falso**.

A continuación se muestra un ejemplo completo que muestra cómo utilizar la propiedad [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) de la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) para ocultar los encabezados de filas y columnas en la primera hoja de un archivo.

La captura de pantalla muestra Book1.xls, el archivo de entrada. Contiene tres hojas de cálculo: Hoja1, Hoja2 y Hoja3. Cada hoja de cálculo muestra los encabezados de filas y columnas.

**Book1.xls: hoja de cálculo antes de la modificación**

![todo:image_alt_text](display-or-hide-row-column-headers-in-aspose-cells_1.png)

Book1.xls se abre llamando al método Open de la clase Workbook y los encabezados de filas y columnas en la primera hoja de cálculo se ocultan. El archivo modificado se guarda como output.xls.

**Output.xls: hoja de cálculo después de la modificación** 

![todo:image_alt_text](display-or-hide-row-column-headers-in-aspose-cells_2.png)

**C#**

{{< highlight csharp >}}

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

## **Descargar Código en Ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Row%20Column%20Headers)

## **Descargar Código de Ejemplo**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}
