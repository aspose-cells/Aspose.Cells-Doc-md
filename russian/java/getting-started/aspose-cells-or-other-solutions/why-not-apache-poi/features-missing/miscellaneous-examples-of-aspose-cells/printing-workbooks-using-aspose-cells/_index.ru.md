---
title: Печать рабочих книг с использованием Aspose.Cells
type: docs
weight: 20
url: /ru/java/printing-workbooks-using-aspose-cells/
---

## **Aspose.Cells - Печать книг**
После того, как вы закончите создание своей электронной таблицы, вам, вероятно, захочется напечатать твердую копию листа по своему усмотрению. Когда вы печатаете, MS Excel предполагает, что вы хотите напечатать всю область листа, если не сделано какого-либо выбор.

Печать Листа

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

Печать Рабочей Книги

**Java**

{{< highlight java >}}

 //Create a WorkbookRender object with respect to your workbook

WorkbookRender wr = new WorkbookRender(book, imgOptions);

//Print the workbook

wr.toPrinter("Samsung ML-1520 Series");

{{< /highlight >}}
## **Скачать работающий код**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Загрузить образец кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/print/AsposePrintWorkbook.java)

{{% alert color="primary" %}} 

Для получения дополнительной информации посетите [Печать рабочих книг](/cells/ru/java/printing-workbooks).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
