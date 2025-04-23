---
title: Agregando Hipervínculos para Vincular Datos en Aspose.Cells
type: docs
weight: 10
url: /es/net/adding-hyperlinks-to-link-data-in-aspose-cells/
---

{{% alert color="primary" %}}

Un hipervínculo se usa para crear un enlace entre dos entidades. Todos están familiarizados con el uso de hipervínculos, especialmente en sitios web.

Utilizando Aspose.Cells, los desarrolladores pueden crear diferentes tipos de hipervínculos en archivos de Microsoft Excel. Este tema discute qué tipos de hipervínculos son compatibles con Aspose.Cells y cómo se pueden usar en nuestros archivos de Excel.

{{% /alert %}}

## **Añadiendo hipervínculos**

Se pueden agregar tres tipos de hipervínculos a una celda utilizando Aspose.Cells:

- [Agregando enlace a una URL](#adding-link-to-a-url).
- [Agregando un enlace a otra celda en el mismo archivo](#adding-a-link-to-a-cell-in-the-same-file).
- [Agregando un enlace a un archivo externo](#adding-a-link-to-an-external-file).

Aspose.Cells permite a los desarrolladores agregar hipervínculos a archivos de Excel ya sea utilizando la API o [hojas de cálculo diseñadas](/cells/es/net/what-is-a-designer-spreadsheet/) (hojas de cálculo donde los hipervínculos se crean manualmente y Aspose.Cells se usa para importarlos a otras hojas de cálculo).

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) que permite acceder a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona diferentes métodos para agregar diferentes hipervínculos a archivos de Excel.

### **Añadir un enlace a una URL**

La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) contiene una colección [**Hyperlinks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks). Cada elemento en la colección de Hipervínculos representa un Hipervínculo. Añade hipervínculos a las URL llamando al método Add de la colección de Hipervínculos. El método Add toma los siguientes parámetros:

- Nombre de la celda, el nombre de la celda a la que se agregará el hipervínculo.
- Número de filas, el número de filas en este rango de hipervínculo.
- Número de columnas, el número de columnas en este rango de hipervínculo.
- URL, la dirección de la URL.

**C#**

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Adding a hyperlink to a URL at "A1" cell

worksheet.Hyperlinks.Add("A1", 1, 1, "http://www.aspose.com");

//Saving the Excel file

workbook.Save("C:\\book1.xls");

{{< /highlight >}}

### **Añadir un enlace a una celda en el mismo archivo**

Es posible agregar hipervínculos a celdas en el mismo archivo de Excel llamando al método Agregar de la colección de hipervínculos. El método Agregar funciona tanto para hipervínculos internos como externos. Una versión del método sobrecargado toma los siguientes parámetros:

- Nombre de la celda, el nombre de la celda a la que se agregará el hipervínculo.
- Número de filas, el número de filas en este rango de hipervínculo.
- Número de columnas, el número de columnas en este rango de hipervínculo.
- URL, la dirección de la celda de destino.

**C#**

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the first (default) worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in

//the same Excel file

worksheet.Hyperlinks.Add("B3", 1, 1, "Sheet2!B9");

//Saving the Excel file

workbook.Save("C:\\book1.xls");

{{< /highlight >}}

### **Agregar un enlace a un archivo externo**

Es posible agregar hipervínculos a archivos externos de Excel llamando al método Add de la colección Hyperlinks. El método Add toma los siguientes parámetros:

- Nombre de la celda, el nombre de la celda a la que se agregará el hipervínculo.
- Número de filas, el número de filas en este rango de hipervínculo.
- Número de columnas, el número de columnas en este rango de hipervínculo.
- URL, la dirección del destino, archivo externo de Excel.

**C#**

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Excel object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in

//the same Excel file

worksheet.Hyperlinks.Add("A5", 1, 1, "C:\\book1.xls");

//Saving the Excel file

workbook.Save("C:\\book2.xls");

{{< /highlight >}}

## **Descargar Código en Ejecución**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Adding%20Hyperlinks%20to%20Link%20Data)

## **Descargar Código de Ejemplo**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}
