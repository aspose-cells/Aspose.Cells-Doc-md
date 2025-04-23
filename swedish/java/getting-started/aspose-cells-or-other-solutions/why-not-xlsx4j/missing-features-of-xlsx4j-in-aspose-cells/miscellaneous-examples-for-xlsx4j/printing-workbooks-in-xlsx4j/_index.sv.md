---
title: Skriva ut arbetsböcker i xlsx4j
type: docs
weight: 30
url: /sv/java/printing-workbooks-in-xlsx4j/
---

## **Aspose.Cells - Skriv ut arbetsböcker**
När du har skapat din kalkylblad vill du förmodligen skriva ut en papperskopia av kalkylarket enligt ditt behov. När du skriver ut antar MS Excel att du vill skriva ut hela kalkylbladsområdet om du inte specificerar ditt urval.

**Skriva ut arbetsblad**

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

**Skriva ut arbetsbok**

**Java**

{{< highlight java >}}

 //Create a WorkbookRender object with respect to your workbook

WorkbookRender wr = new WorkbookRender(book, imgOptions);

//Print the workbook

wr.toPrinter("Samsung ML-1520 Series");

{{< /highlight >}}
## **Ladda ned körbar kod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/print/printworkbook/AsposePrintWorkbook.java)

{{% alert color="primary" %}} 

För mer information, besök [Skriva ut arbetsböcker ](/cells/sv/java/skriva-ut-arbetsboker).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
