---
title: 在Aspose.Cells中打印工作簿
type: docs
weight: 20
url: /zh/net/printing-workbooks-in-aspose-cells/
---

## **Aspose.Cells - 打印工作簿**
完成创建电子表格后，您可能希望打印工作表的硬拷贝以满足您的需求。在打印时，MS Excel会假定您要打印整个工作表区域，除非您指定您的选择。

打印工作表

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
## **下载运行代码**
从以下所列的社交编码站点下载**打印工作簿** 表单:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Printing.Workbooks.Aspose.Cells.zip)

{{% alert color="primary" %}} 

要了解更多详细信息，请访问[打印工作簿](/cells/zh/net/printing-workbooks/)。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
