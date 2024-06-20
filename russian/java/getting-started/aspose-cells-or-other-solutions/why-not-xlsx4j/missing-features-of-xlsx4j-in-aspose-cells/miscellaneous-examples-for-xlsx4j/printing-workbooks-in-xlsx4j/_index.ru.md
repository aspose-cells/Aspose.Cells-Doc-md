---
title: Печать книг в xlsx4j
type: docs
weight: 30
url: /ru/java/printing-workbooks-in-xlsx4j/
---

## **Aspose.Cells - Печать книг**
После того, как вы закончите создание своей электронной таблицы, вам, вероятно, захочется напечатать твердую копию листа по своему усмотрению. Когда вы печатаете, MS Excel предполагает, что вы хотите напечатать всю область листа, если не сделано какого-либо выбор.

 **Печать листа**

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

 **Печать книги**

**Java**

{{< highlight java >}}

 //Create a WorkbookRender object with respect to your workbook

WorkbookRender wr = new WorkbookRender(book, imgOptions);

//Print the workbook

wr.toPrinter("Samsung ML-1520 Series");

{{< /highlight >}}
## **Скачать работающий код**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Загрузить образец кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/print/printworkbook/AsposePrintWorkbook.java)

{{% alert color="primary" %}} 

Для получения более подробной информации посетите [Печать Рабочих Книг](/cells/ru/java/printing-workbooks).

{{% /alert %}}
