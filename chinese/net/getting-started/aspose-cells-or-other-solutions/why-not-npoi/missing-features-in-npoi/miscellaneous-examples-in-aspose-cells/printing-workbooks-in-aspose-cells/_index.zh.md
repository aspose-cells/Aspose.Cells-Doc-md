---
title: 打印工作簿 Aspose.Cells
type: docs
weight: 20
url: /zh/net/printing-workbooks-in-aspose-cells/
---
## **Aspose.Cells - 打印工作簿**
完成电子表格创建后，您可能需要根据需要打印一份工作表的硬拷贝。打印时，MS Excel 假定您要打印整个工作表区域，除非您指定了您的选择。

打印工作表

**C#**

{{< highlight "cs" >}}

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
下载**打印工作簿**形成以下任何一个社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Printing.Workbooks.Aspose.Cells.zip)

{{% alert color="primary" %}} 

欲了解更多详情，请访问[打印工作簿](/cells/zh/net/printing-workbooks/).

{{% /alert %}}
