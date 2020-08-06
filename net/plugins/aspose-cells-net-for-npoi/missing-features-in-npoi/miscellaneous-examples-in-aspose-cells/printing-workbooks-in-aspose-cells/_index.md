---
title: Printing Workbooks in Aspose.Cells
type: docs
weight: 20
url: /net/printing-workbooks-in-aspose-cells/
---

## **Aspose.Cells - Printing Workbooks**
After you finish creating your spreadsheet, you will probably want to print a hard copy of the sheet for your need. When you are printing, MS Excel assumes you want to print the entire worksheet area unless you specify your selection.

Printing Worksheet

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
## **Download Running Code**
Download **Printing Workbooks** form any of the below mentioned social coding sites:

- [CodePlex](https://asposenpoi.codeplex.com/downloads/get/1482192)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Printing.Workbooks.Aspose.Cells.zip)

{{% alert color="primary" %}} 

For more details, visit [Printing Workbooks](http://www.aspose.com/docs/display/cellsnet/Printing+Workbooks).

{{% /alert %}}
