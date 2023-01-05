---
title: Imprimir libros de trabajo en xlsx4j
type: docs
weight: 30
url: /es/java/printing-workbooks-in-xlsx4j/
---
## **Aspose.Cells - Cuadernos de impresión**
Después de que termine de crear su hoja de cálculo, probablemente querrá imprimir una copia impresa de la hoja para su necesidad. Cuando está imprimiendo, MS Excel asume que desea imprimir el área completa de la hoja de trabajo a menos que especifique su selección.

**Hoja de trabajo de impresión**

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook

Workbook book = new Workbook(dataDir + "AsposeDataInput.xls");

//Create an object for ImageOptions

ImageOrPrintOptions  imgOptions = new ImageOrPrintOptions ();

//Get the first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Create a SheetRender object with respect to your desired sheet

SheetRender sr = new SheetRender(sheet, imgOptions);

//Print the worksheet

sr.toPrinter("Samsung ML-1520 Series");

{{< /highlight >}}

**Imprimir libro de trabajo**

**Java**

{{< highlight "java" >}}

 //Create a WorkbookRender object with respect to your workbook

WorkbookRender wr = new WorkbookRender(book, imgOptions);

//Print the workbook

wr.toPrinter("Samsung ML-1520 Series");

{{< /highlight >}}
## **Descargar código de ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/print/printworkbook/AsposePrintWorkbook.java)

{{% alert color="primary" %}} 

 Para más detalles, visite[ Impresión de libros de trabajo](/cells/es/java/printing-workbooks).

{{% /alert %}}
