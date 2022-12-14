---
title: Skriva ut arbetsböcker med Aspose.Cells
type: docs
weight: 20
url: /sv/java/printing-workbooks-using-aspose-cells/
---
## **Aspose.Cells - Skriva ut arbetsböcker**
När du har skapat ditt kalkylblad vill du antagligen skriva ut en papperskopia av bladet för ditt behov. När du skriver ut antar MS Excel att du vill skriva ut hela kalkylbladet om du inte anger ditt val.

Skriva ut arbetsblad

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

Utskrift av arbetsbok

**Java**

{{< highlight "java" >}}

 //Create a WorkbookRender object with respect to your workbook

WorkbookRender wr = new WorkbookRender(book, imgOptions);

//Print the workbook

wr.toPrinter("Samsung ML-1520 Series");

{{< /highlight >}}
## **Ladda ner Running Code**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ner exempelkod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/print/AsposePrintWorkbook.java)

{{% alert color="primary" %}} 

 För mer information, besök[Skriva ut arbetsböcker](/cells/sv/java/printing-workbooks).

{{% /alert %}}
