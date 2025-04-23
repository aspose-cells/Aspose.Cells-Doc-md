---
title: Imprimir Libros de Trabajo usando Aspose.Cells
type: docs
weight: 20
url: /es/java/printing-workbooks-using-aspose-cells/
---

## **Aspose.Cells - Impresión de libros de trabajo**
Después de terminar de crear su hoja de cálculo, probablemente querrá imprimir una copia en papel de la hoja para sus necesidades. Al imprimir, MS Excel supone que desea imprimir toda el área de la hoja de cálculo a menos que especifique su selección.

Impresión de hojas de cálculo

**Java**

{{< highlight java >}}

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

Imprimir Libro de Trabajo

**Java**

{{< highlight java >}}

 //Create a WorkbookRender object with respect to your workbook

WorkbookRender wr = new WorkbookRender(book, imgOptions);

//Print the workbook

wr.toPrinter("Samsung ML-1520 Series");

{{< /highlight >}}
## **Descargar Código en Ejecución**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar Código de Ejemplo**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/print/AsposePrintWorkbook.java)

{{% alert color="primary" %}} 

Para más detalles, visita [Imprimir Libros de Trabajo](/cells/es/java/printing-workbooks).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
