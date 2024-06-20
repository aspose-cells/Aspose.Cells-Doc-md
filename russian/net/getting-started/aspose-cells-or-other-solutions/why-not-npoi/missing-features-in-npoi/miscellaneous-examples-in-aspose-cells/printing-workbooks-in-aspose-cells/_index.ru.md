---
title: Печать рабочих книг в Aspose.Cells
type: docs
weight: 20
url: /ru/net/printing-workbooks-in-aspose-cells/
---

## **Aspose.Cells - Печать книг**
После того, как вы закончите создание своей электронной таблицы, вам, вероятно, захочется напечатать твердую копию листа по своему усмотрению. Когда вы печатаете, MS Excel предполагает, что вы хотите напечатать всю область листа, если не сделано какого-либо выбор.

Печать Листа

**C#**

{{< highlight cs >}}

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
## **Скачать работающий код**
Скачать **Печать рабочих книг** с любого из упомянутых ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Printing.Workbooks.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Для получения более подробной информации посетите [Печать рабочих книг](/cells/ru/net/printing-workbooks/).

{{% /alert %}}
