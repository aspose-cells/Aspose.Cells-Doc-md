---
title: Impresión de libros de trabajo en Aspose.Cells
type: docs
weight: 20
url: /es/net/printing-workbooks-in-aspose-cells/
---
## **Aspose.Cells - Cuadernos de impresión**
Después de que termine de crear su hoja de cálculo, probablemente querrá imprimir una copia impresa de la hoja para su necesidad. Cuando está imprimiendo, MS Excel asume que desea imprimir el área completa de la hoja de trabajo a menos que especifique su selección.

Hoja de trabajo de impresión

**C#**

{{< highlight "cs" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Create an object for ImageOptions

ImageOrPrintOptions imgOptions = new ImageOrPrintOptions();

//Get the first worksheet

Worksheet sheet = workbook.Worksheets[0];

//Create a SheetRender object with respect to your desired sheet

SheetRender sr = new SheetRender(sheet, imgOptions);

//Print the worksheet

sr.ToPrinter("Samsung ML-1520 Series");

{{< /highlight >}}
## **Descargar código de ejecución**
 Descargar**Impresión de libros de trabajo** formar cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Printing.Workbooks.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Para más detalles, visite[Impresión de libros de trabajo](/cells/es/net/printing-workbooks/).

{{% /alert %}}
