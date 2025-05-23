---
title: Arbeitsmappen in xlsx4j drucken
type: docs
weight: 30
url: /de/java/printing-workbooks-in-xlsx4j/
---

## **Aspose.Cells - Arbeitsmappen drucken**
Nachdem Sie Ihre Arbeitsmappe erstellt haben, möchten Sie wahrscheinlich eine gedruckte Version des Blatts für Ihre Zwecke haben. Beim Drucken geht MS Excel davon aus, dass Sie den gesamten Arbeitsblattbereich drucken möchten, es sei denn, Sie geben Ihre Auswahl an.

**Arbeitsblatt drucken**

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

**Arbeitsmappe drucken**

**Java**

{{< highlight java >}}

 //Create a WorkbookRender object with respect to your workbook

WorkbookRender wr = new WorkbookRender(book, imgOptions);

//Print the workbook

wr.toPrinter("Samsung ML-1520 Series");

{{< /highlight >}}
## **Laufenden Code herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/print/printworkbook/AsposePrintWorkbook.java)

{{% alert color="primary" %}} 

Besuchen Sie für weitere Details [Arbeitsmappen drucken](/cells/de/java/printing-workbooks).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
